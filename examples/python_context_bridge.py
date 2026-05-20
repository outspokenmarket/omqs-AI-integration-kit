"""
OMQS Signal-to-LLM Context Bridge.

This example converts an OMQS candle or snapshot into clear text that can be
pasted into a large language model.

Run:
    python examples/python_context_bridge.py
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

BASE_DIR = Path(__file__).resolve().parent


def to_float(value: Any) -> Optional[float]:
    if value is None:
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def signal_label(value: Any) -> str:
    if value == 1:
        return "blue / long-bias regime"
    if value == -1:
        return "red / short-bias regime"
    return "signal unavailable"


def candle_datetime(timestamp: Any) -> str:
    if timestamp is None:
        return "unavailable"
    try:
        return datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M:%S")
    except (TypeError, ValueError, OSError):
        return "unavailable"


def normalize_candle(message: Dict[str, Any], symbol: Optional[str] = None, timeframe: Optional[str] = None) -> Dict[str, Any]:
    stops = message.get("stops") or {}
    omqs = message.get("omqs")

    return {
        "symbol": message.get("symbol") or symbol,
        "timeframe": message.get("timeframe") or timeframe,
        "timestamp": message.get("timestamp"),
        "datetime": candle_datetime(message.get("timestamp")),
        "open": to_float(message.get("open")),
        "high": to_float(message.get("high")),
        "low": to_float(message.get("low")),
        "close": to_float(message.get("close")),
        "volume": to_float(message.get("volume")),
        "closed": message.get("closed"),
        "omqs": omqs,
        "signal_label": signal_label(omqs),
        "stop": to_float(message.get("stop")),
        "stop_fast": to_float(stops.get("fast")),
        "stop_balanced": to_float(stops.get("balanced")),
        "stop_slow": to_float(stops.get("slow")),
    }


def extract_candles(message: Dict[str, Any]) -> List[Dict[str, Any]]:
    if message.get("type") == "snapshot":
        symbol = message.get("symbol")
        timeframe = message.get("timeframe")
        return [normalize_candle(item, symbol=symbol, timeframe=timeframe) for item in message.get("ohlc", [])]

    if message.get("type") == "candle":
        return [normalize_candle(message)]

    return []


def market_state_to_text(candle: Dict[str, Any]) -> str:
    closed = candle.get("closed")
    if closed is True:
        candle_status = "closed candle, finalized for this timeframe"
    elif closed is False:
        candle_status = "open candle, still forming"
    else:
        candle_status = "candle status unavailable"

    lines = [
        "OMQS MARKET STATE",
        "",
        f"Symbol: {candle.get('symbol')}",
        f"Timeframe: {candle.get('timeframe')}",
        f"Datetime: {candle.get('datetime')}",
        f"Open: {candle.get('open')}",
        f"High: {candle.get('high')}",
        f"Low: {candle.get('low')}",
        f"Close: {candle.get('close')}",
        f"Volume: {candle.get('volume')}",
        f"Candle status: {candle_status}",
        f"OMQS signal: {candle.get('omqs')} ({candle.get('signal_label')})",
        f"Default stop: {candle.get('stop')}",
        f"Fast stop: {candle.get('stop_fast')}",
        f"Balanced stop: {candle.get('stop_balanced')}",
        f"Slow stop: {candle.get('stop_slow')}",
        "",
        "Interpretation context:",
        f"The model currently classifies this market as {candle.get('signal_label')}.",
        "Use this as quantitative market context, not as a guarantee of future price direction.",
    ]

    if closed is False:
        lines.append("Because the candle is still open, the values may change before the candle closes.")
    elif closed is True:
        lines.append("Because the candle is closed, the values are finalized for that candle.")

    return "\n".join(lines)


def build_llm_prompt(candles: Iterable[Dict[str, Any]]) -> str:
    blocks = [market_state_to_text(candle) for candle in candles]
    return "\n\n" + ("-" * 72) + "\n\n".join(blocks)


def main() -> None:
    sample_path = BASE_DIR / "sample_candle.json"
    message = json.loads(sample_path.read_text(encoding="utf-8"))
    candles = extract_candles(message)
    print(build_llm_prompt(candles))


if __name__ == "__main__":
    main()
