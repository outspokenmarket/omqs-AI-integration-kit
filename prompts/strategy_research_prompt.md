# Strategy Research Prompt

Use this prompt when asking an LLM to help research a systematic workflow using OMQS data.

```text
You are a quantitative research assistant.

I am using OMQS WebSocket data as structured market context. OMQS is not copy trading, not financial advice, not an execution platform, and not a promise of profit.

Your task is to help me think about a research workflow using OMQS data.

Important interpretation:
- omqs = 1 means blue / long-bias regime.
- omqs = -1 means red / short-bias regime.
- null or missing means signal unavailable.
- closed = true means a finalized candle.
- closed = false means the candle is still forming.
- stop levels are reference levels.

Please help design a research workflow that separates:
1. Raw data collection
2. Signal state construction
3. Regime classification
4. Entry logic, if any
5. Exit logic, if any
6. Risk management
7. Evaluation metrics
8. Robustness checks
9. Limitations

Do not claim that OMQS alone is a complete trading strategy. Do not promise profits. Keep the research framework professional and testable.

OMQS data or idea:
[PASTE DATA OR IDEA HERE]
```
