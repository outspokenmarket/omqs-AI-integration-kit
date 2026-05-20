# Sample LLM Analysis

## Input

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

## Output

BTCUSDT on timeframe 1 is currently in a blue long-bias regime according to the latest OMQS update. The candle is still open, so this should be treated as live market context rather than finalized candle confirmation. The latest close is 81012.80, with the default stop reference at 80120.55. The fast, balanced, and slow stop references are available and can be used as context for monitoring or alerting. This signal does not guarantee future price direction and should not be treated as financial advice.
