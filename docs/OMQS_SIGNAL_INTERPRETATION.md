# OMQS Signal Interpretation

This document explains how to interpret OMQS WebSocket data when building dashboards, alerts, journals, market summaries, or LLM workflows.

## Core idea

OMQS should be treated as a quantitative regime and directional-bias signal.

It is designed to help structure market interpretation in a consistent and repeatable way. It should not be interpreted as a promise of profit, a guarantee of direction, or an execution command.

## Signal values

| Value | Visual meaning | Practical interpretation |
| --- | --- | --- |
| `1` | Blue | Long-bias regime |
| `-1` | Red | Short-bias regime |
| `null` or missing | Unavailable | No usable signal available in that message |

## How to speak about the signal

Preferred language:

- Long-bias regime
- Short-bias regime
- Quantitative regime signal
- Model classification
- Market interpretation framework
- Signal confirmation on a closed candle
- Signal still updating on an open candle
- Stop reference level
- Fast, balanced, or slow stop regime

Avoid language such as:

- Guaranteed trade
- Buy now
- Sell now
- Profit signal
- Prediction that cannot fail
- Financial advice
- Risk-free opportunity

## Closed candles versus open candles

A candle with:

```text
closed = true
```

is finalized for that timeframe.

A candle with:

```text
closed = false
```

is still forming. It may change before the candle closes.

For alerting and research, many users may prefer to trigger stronger confirmations only on closed candles. For monitoring and dashboards, open candle updates are still useful because they show the current live state.

## Stop levels

The API may return:

```text
stop
stops.fast
stops.balanced
stops.slow
```

These are reference levels that can be used for context, monitoring, and risk awareness.

General framing:

- `fast`: more reactive reference level
- `balanced`: default or middle reference level
- `slow`: slower and less reactive reference level
- `stop`: default stop reference returned by the API

These levels should not be presented as guarantees or as isolated trading instructions.

## Cross-timeframe context

When multiple timeframes are monitored, useful LLM summaries may compare:

- Whether different timeframes agree or disagree
- Whether a lower timeframe changed before a higher timeframe
- Whether the latest update is closed or still forming
- Whether price is above or below stop reference levels
- Whether the signal appears stable or transitioning

Example wording:

```text
BTCUSDT M5 is currently in a blue long-bias regime, while H1 remains unavailable. The latest M5 candle is still open, so the signal should be treated as live context rather than a finalized confirmation.
```

## Practical use cases

OMQS signals can support:

- Market monitoring
- Automated alerts
- Dashboard construction
- Trading journal entries
- Quantitative research
- Strategy filters
- LLM-generated summaries
- Workflow automation

OMQS signals should not be used as:

- Blind execution commands
- Guarantees of future market movement
- A replacement for risk management
- Standalone financial advice
