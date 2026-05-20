# OMQS Safety and Usage Guide

This guide defines safe and professional usage principles for OMQS WebSocket data, especially when combined with large language models.

## Correct positioning

OMQS provides quantitative market signals and model outputs that can be used for market interpretation, monitoring, research, alerting, dashboards, and decision support.

OMQS is not:

- Copy trading
- A broker
- An execution platform
- A guarantee of profit
- A replacement for risk management
- Financial advice

## API key safety

Never paste an API key into an LLM chat.

Never hardcode an API key into a public script.

Never commit `.env` to GitHub.

Use this pattern:

```text
OMQS_WS_API_KEY=your_websocket_api_key_here
OMQS_WS_URL=wss://om-qs.com/ws/api/v1/models/
```

## LLM safety rules

When asking an LLM to analyze OMQS data, instruct it to:

- Treat OMQS as decision-support context.
- Avoid financial advice.
- Avoid guaranteed statements.
- Distinguish closed candles from open candles.
- Clearly identify unavailable or missing values.
- Use neutral professional language.
- Avoid recommending oversized positions.
- Avoid presenting signals as automatic execution commands.

## Recommended language

Good:

```text
The latest BTCUSDT M5 candle is closed and OMQS is blue, indicating a long-bias regime according to the current model output.
```

Bad:

```text
Buy BTC now because the model guarantees that price will rise.
```

## Best practices for alerts

Alerts should describe a condition, not promise an outcome.

Good alert:

```text
BTCUSDT M5 closed with OMQS blue. Close is above the balanced stop. This indicates a confirmed long-bias regime for this timeframe.
```

Poor alert:

```text
BTCUSDT buy signal. Guaranteed profit setup.
```

## Best practices for journals

A journal should describe what the system observed.

Useful fields:

- Symbol
- Timeframe
- Timestamp
- Candle status
- OMQS signal
- Close price
- Stop references
- Prior signal if available
- Interpretation
- Risk note

## Best practices for research

When using OMQS data in research, separate:

- raw input data
- signal interpretation
- trading rules
- position sizing
- risk controls
- performance evaluation

Do not assume that an OMQS signal alone defines a complete trading strategy.
