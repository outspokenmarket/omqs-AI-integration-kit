# Recipe: Build a Trading Journal

This recipe shows how to transform OMQS WebSocket updates into structured trading journal entries.

## Goal

Create journal entries from OMQS candle updates.

Each entry should record:

- Date and time
- Symbol
- Timeframe
- Candle status
- Close price
- OMQS signal
- Signal interpretation
- Stop reference
- Fast, balanced, and slow stops
- Optional comment
- Risk note

## Journal entry template

```text
Date/time: 2026-05-19 12:00:00
Symbol: BTCUSDT
Timeframe: M5
Close: 81012.80
Candle: closed
OMQS: 1, blue / long-bias regime
Stop: 80120.55
Fast stop: 80310.10
Balanced stop: 80120.55
Slow stop: 79880.40
Interpretation: The model classifies this market as long-bias on this timeframe.
Risk note: This is a quantitative regime signal, not a guarantee of future price direction.
```

## LLM prompt

Use `prompts/trading_journal_prompt.md` to generate more polished journal entries.

## Useful journal questions

Ask the LLM:

```text
Create a professional journal entry from this OMQS update. Focus on signal interpretation, candle status, stop context, and what changed versus the previous update.
```

## Important separation

Keep separate:

1. OMQS state
2. Your discretionary idea
3. Your execution decision
4. Your risk management
5. Your post-trade review

This makes the journal more useful and avoids confusing signal context with execution logic.
