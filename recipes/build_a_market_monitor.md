# Recipe: Build a Market Monitor

This recipe shows how to build a simple market monitor using the OMQS WebSocket API.

## Goal

Create a script that:

1. Connects to the OMQS WebSocket API.
2. Authenticates with your WebSocket API key.
3. Subscribes to selected pairs.
4. Receives snapshots and live candle updates.
5. Prints the latest OMQS state every few seconds.
6. Keeps the session alive by replying to `ping` with `pong`.

## Recommended files

```text
market_monitor/
├── .env
├── .gitignore
├── market_monitor.py
└── requirements.txt
```

## Environment variables

```text
OMQS_WS_API_KEY=your_websocket_api_key_here
OMQS_WS_URL=wss://om-qs.com/ws/api/v1/models/
```

## Suggested pairs

Start small:

```text
BTCUSDT 1m
ETHUSDT 5m
EURUSD 5m
```

After the monitor works, add more pairs while respecting the API limits.

## Display format

A clean monitor should print:

```text
BTCUSDT | TF 1 | Close: 81012.80 | OMQS: 1 (blue / long-bias regime) | Closed: false | Stop: 80120.55
```

## LLM extension

Once the monitor works, you can convert each update into an LLM-readable text block:

```text
BTCUSDT M1 is currently in a blue long-bias regime. The candle is still open, so this is live context rather than finalized confirmation. The latest close is above the balanced stop reference.
```

## Safety note

The market monitor should describe current model state. It should not output financial advice, trade guarantees, or automatic execution commands.
