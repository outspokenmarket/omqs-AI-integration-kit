"""
OMQS WebSocket API console client.

This example:
- loads the API key from .env
- connects to the OMQS WebSocket API
- authenticates after hello
- subscribes to example pairs
- responds to ping with pong
- prints the latest market state every 5 seconds

Run:
    pip install -r requirements.txt
    python examples/python_console_client.py
"""

import json
import os
import threading
import time
from collections import defaultdict, deque
from datetime import datetime

import websocket
from dotenv import load_dotenv

load_dotenv(override=True)

OMQS_WS_API_KEY = os.getenv("OMQS_WS_API_KEY")
OMQS_WS_URL = os.getenv("OMQS_WS_URL", "wss://om-qs.com/ws/api/v1/models/")

if not OMQS_WS_API_KEY:
    raise RuntimeError("Set OMQS_WS_API_KEY in your .env file or environment.")

OMQS_PAIRS = [
    {"model": "crypto", "ticker": "BTCUSDT", "timeframe": "1m"},
    {"model": "crypto", "ticker": "ETHUSDT", "timeframe": "5m"},
    {"model": "forex", "ticker": "EURUSD", "timeframe": "5m"},
]

lock = threading.Lock()
latest = {}
history = defaultdict(lambda: deque(maxlen=500))
status = {
    "connected": False,
    "authenticated": False,
    "subscribed": False,
    "connection_id": None,
    "last_message_at": None,
    "last_error": None,
}


def now_utc() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")


def to_float(value):
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return value


def signal_label(value) -> str:
    if value == 1:
        return "blue / long-bias regime"
    if value == -1:
        return "red / short-bias regime"
    return "signal unavailable"


def normalize_candle(message: dict) -> dict:
    timestamp = message.get("timestamp")
    candle_time = None
    if timestamp is not None:
        candle_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")

    stops = message.get("stops") or {}

    return {
        "received_at": now_utc(),
        "symbol": message.get("symbol"),
        "timeframe": message.get("timeframe"),
        "timestamp": timestamp,
        "datetime": candle_time,
        "open": to_float(message.get("open")),
        "high": to_float(message.get("high")),
        "low": to_float(message.get("low")),
        "close": to_float(message.get("close")),
        "volume": to_float(message.get("volume")),
        "closed": message.get("closed"),
        "omqs": message.get("omqs"),
        "signal_label": signal_label(message.get("omqs")),
        "stop": to_float(message.get("stop")),
        "stop_fast": to_float(stops.get("fast")),
        "stop_balanced": to_float(stops.get("balanced")),
        "stop_slow": to_float(stops.get("slow")),
    }


def store_candle(candle: dict) -> None:
    key = (candle["symbol"], candle["timeframe"])
    with lock:
        latest[key] = candle
        history[key].append(candle)
        status["last_message_at"] = now_utc()


def get_latest() -> list[dict]:
    with lock:
        return list(latest.values())


def get_status() -> dict:
    with lock:
        return dict(status)


def websocket_loop() -> None:
    ws = None
    try:
        ws = websocket.create_connection(OMQS_WS_URL, timeout=15)

        with lock:
            status["connected"] = True
            status["last_error"] = None

        while True:
            raw = ws.recv()
            if not raw:
                break

            message = json.loads(raw)
            message_type = message.get("type")

            with lock:
                status["last_message_at"] = now_utc()

            if message_type == "hello":
                ws.send(json.dumps({"type": "auth", "api_key": OMQS_WS_API_KEY}))

            elif message_type == "ready":
                with lock:
                    status["authenticated"] = True
                    status["connection_id"] = message.get("connection_id")

                ws.send(json.dumps({
                    "type": "subscribe",
                    "request_id": "console-subscription",
                    "pairs": OMQS_PAIRS,
                }))

            elif message_type == "subscribed":
                with lock:
                    status["subscribed"] = True

            elif message_type == "ping":
                ws.send(json.dumps({"type": "pong"}))

            elif message_type == "snapshot":
                symbol = message.get("symbol")
                timeframe = message.get("timeframe")

                for item in message.get("ohlc", []):
                    item["symbol"] = symbol
                    item["timeframe"] = timeframe
                    store_candle(normalize_candle(item))

            elif message_type == "candle":
                store_candle(normalize_candle(message))

            elif message_type == "error":
                with lock:
                    status["last_error"] = message
                print("OMQS error:", message)

    except Exception as exc:
        with lock:
            status["connected"] = False
            status["last_error"] = str(exc)
        print("WebSocket stopped with error:", exc)

    finally:
        if ws is not None:
            try:
                ws.close()
            except Exception:
                pass
        with lock:
            status["connected"] = False


def print_monitor() -> None:
    while True:
        current_status = get_status()
        rows = sorted(get_latest(), key=lambda x: (x.get("symbol") or "", x.get("timeframe") or ""))

        print("\n" + "=" * 72)
        print("OMQS WebSocket status")
        print("=" * 72)
        print(f"Connected:     {current_status.get('connected')}")
        print(f"Authenticated: {current_status.get('authenticated')}")
        print(f"Subscribed:    {current_status.get('subscribed')}")
        print(f"Connection ID: {current_status.get('connection_id')}")
        print(f"Last message:  {current_status.get('last_message_at')}")
        print(f"Last error:    {current_status.get('last_error')}")

        if not rows:
            print("\nWaiting for data...")
        else:
            print("\nLatest OMQS data")
            print("-" * 72)
            for item in rows:
                print(
                    f"{item.get('symbol')} | "
                    f"TF {item.get('timeframe')} | "
                    f"Close: {item.get('close')} | "
                    f"OMQS: {item.get('omqs')} ({item.get('signal_label')}) | "
                    f"Closed: {item.get('closed')} | "
                    f"Stop: {item.get('stop')}"
                )

        time.sleep(5)


def main() -> None:
    thread = threading.Thread(target=websocket_loop, daemon=True)
    thread.start()
    print_monitor()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped by user.")
