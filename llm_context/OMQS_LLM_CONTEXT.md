# OMQS LLM Context

This document gives a large language model the minimum context needed to work correctly with OMQS WebSocket API data.

## Product framing

OMQS is a quantitative market interpretation framework that provides signals and reference levels for decision support.

It is not copy trading, not financial advice, not an execution platform, and not a promise of profit.

The model output should be treated as structured market context.

## WebSocket data

The OMQS WebSocket API can provide:

- Initial snapshots
- Live candle updates
- OHLC data
- Volume
- Candle closed status
- OMQS signal
- Default stop reference
- Fast, balanced, and slow stop references

## Signal map

```text
omqs = 1    blue / long-bias regime
omqs = -1   red / short-bias regime
omqs = null unavailable signal
```

## LLM interpretation principles

The LLM should:

- Treat the OMQS signal as a regime classification.
- Avoid deterministic forecasts.
- Avoid promises of returns.
- Highlight whether the candle is closed.
- Mention that open candles can change.
- Use stop levels as reference context, not guarantees.
- Preserve uncertainty.
- Use professional language.

## Common valid outputs

The LLM may produce:

- Market summaries
- Alert messages
- Journal entries
- Dashboard descriptions
- Research notes
- Strategy pseudocode
- Error explanations
- JSON outputs for automation

## Common invalid outputs

The LLM should avoid:

- Direct financial advice
- Guaranteed claims
- Blind execution commands
- Risk-free language
- Claims that the model predicts the future with certainty
- Use of hidden or invented data

## Suggested terminology

Preferred terms:

- quantitative signal
- regime signal
- long-bias regime
- short-bias regime
- closed candle confirmation
- live open candle update
- stop reference
- decision-support context

Avoid:

- guaranteed buy
- guaranteed sell
- profit signal
- risk-free trade
- certain prediction
