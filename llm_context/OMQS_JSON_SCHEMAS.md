# OMQS JSON Schemas

This document describes the expected shape of common OMQS WebSocket messages.

These are practical schemas for LLMs and developers. They are not formal JSON Schema draft files.

## Auth message

Client to server:

```json
{
  "type": "auth",
  "api_key": "your_websocket_api_key_here"
}
```

## Subscribe message

Client to server:

```json
{
  "type": "subscribe",
  "request_id": "sub-main",
  "pairs": [
    {
      "model": "crypto",
      "ticker": "BTCUSDT",
      "timeframe": "1m"
    }
  ]
}
```

## Pair object

```json
{
  "model": "crypto",
  "ticker": "BTCUSDT",
  "timeframe": "1m"
}
```

Fields:

- `model`: market family or data group, such as `crypto`, `forex`, `b3_futures`, `b3_stocks`, `nasdaq`, `international`, or `us_futures`.
- `ticker`: instrument identifier.
- `timeframe`: requested timeframe, such as `1m`, `5m`, or `15m` when enabled.

## Snapshot message

Server to client:

```json
{
  "type": "snapshot",
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "ohlc": [
    {
      "timestamp": 1774915200,
      "open": "80920.00",
      "high": "81020.00",
      "low": "80880.00",
      "close": "80988.41",
      "volume": "24.18",
      "closed": true,
      "omqs": 1,
      "stop": "80120.55",
      "stops": {
        "fast": "80310.10",
        "balanced": "80120.55",
        "slow": "79880.40"
      }
    }
  ],
  "omqs": 1,
  "stop": "80120.55",
  "stops": {
    "fast": "80310.10",
    "balanced": "80120.55",
    "slow": "79880.40"
  }
}
```

## Candle message

Server to client:

```json
{
  "type": "candle",
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "timestamp": 1774915260,
  "open": "80988.41",
  "high": "81044.20",
  "low": "80970.00",
  "close": "81012.80",
  "volume": "18.42",
  "closed": false,
  "omqs": 1,
  "stop": "80120.55",
  "stops": {
    "fast": "80310.10",
    "balanced": "80120.55",
    "slow": "79880.40"
  }
}
```

## Candle field guide

| Field | Type | Meaning |
| --- | --- | --- |
| `type` | string | Message type, usually `snapshot` or `candle`. |
| `symbol` | string | Market identifier. |
| `timeframe` | string | Normalized chart timeframe. |
| `timestamp` | integer | Unix timestamp for candle open time. |
| `open` | string or number | Candle open price. |
| `high` | string or number | Candle high price. |
| `low` | string or number | Candle low price. |
| `close` | string or number | Candle close or current close value. |
| `volume` | string or number | Volume when available. |
| `closed` | boolean | Whether the candle is finalized. |
| `omqs` | integer or null | OMQS signal. `1` means blue / long-bias. `-1` means red / short-bias. |
| `stop` | string or number | Default stop reference. |
| `stops.fast` | string or number | More reactive stop reference. |
| `stops.balanced` | string or number | Balanced stop reference. |
| `stops.slow` | string or number | Slower stop reference. |

## LLM-ready normalized market state

A recommended normalized object for LLM workflows:

```json
{
  "symbol": "BTCUSDT",
  "timeframe": "1",
  "datetime": "2026-05-19 12:00:00",
  "close": 81012.8,
  "closed": false,
  "omqs": 1,
  "signal_label": "blue / long-bias regime",
  "stop": 80120.55,
  "stop_fast": 80310.1,
  "stop_balanced": 80120.55,
  "stop_slow": 79880.4,
  "interpretation_note": "Live open candle update. Treat as current market context, not finalized confirmation."
}
```
