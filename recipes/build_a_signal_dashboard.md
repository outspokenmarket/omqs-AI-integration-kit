# Recipe: Build a Signal Dashboard

This recipe explains how to use OMQS WebSocket data in a dashboard.

## Goal

Build a dashboard that displays:

- Symbol
- Timeframe
- Latest close
- OMQS signal
- Signal color
- Candle status
- Stop references
- Last update time

## Data model

A normalized dashboard row can look like this:

```json
{
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "close": 81012.8,
  "closed": false,
  "omqs": 1,
  "signal_label": "blue / long-bias regime",
  "stop": 80120.55,
  "stop_fast": 80310.1,
  "stop_balanced": 80120.55,
  "stop_slow": 79880.4,
  "last_update": "2026-05-19 12:00:00 UTC"
}
```

## Visual rules

Suggested mapping:

```text
omqs = 1    blue state
omqs = -1   red state
omqs = null neutral or unavailable state
```

Suggested dashboard labels:

- Blue / long-bias regime
- Red / short-bias regime
- Signal unavailable
- Open candle
- Closed candle

## Useful sections

A good dashboard can include:

1. Latest signal table
2. Signal changes
3. Closed candle confirmations
4. Assets with unavailable data
5. Stop reference levels
6. Connection status

## LLM extension

You can add a button that converts the dashboard state into text for an LLM:

```text
Summarize the current OMQS dashboard state. Focus on assets with closed candles, signal changes, and stop context. Do not provide financial advice.
```

## Safety note

The dashboard should present market context and model state. It should not imply guaranteed outcomes.
