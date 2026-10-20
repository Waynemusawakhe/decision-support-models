# Decision Support Models: MzansiFit Uniforms & Services

Quantitative decision models built in Excel for a virtual business, **MzansiFit Uniforms & Services** (school uniform sets, corporate workwear, hospitality attire), in CMPG322 Decision Support Systems 2 (NWU, 2025). Each workbook answers a business question with a standard management-science technique.

| Workbook | Business question | Techniques | Decision |
|---|---|---|---|
| [01 Decision analysis and forecasting](workbooks/01-decision-analysis-and-forecasting.xlsx) | Which investment suits each investor? Stay at the current venue after rate increases, or move? What will next month's sales be? | Decision tables (maximin, EMV), expected value of perfect and sample information, decision trees, trend-line regression, exponential smoothing with trend (MAD, MSE) | Corporate bonds for the risk-averse investor; don't pay R5,000 for market research worth at most R1,200; stay at the venue; forecast with exponential smoothing (α = 0.8, β = 0.2) |
| [02 Inventory and project crashing](workbooks/02-inventory-eoq-and-project-crashing.xlsx) | How much stock to order and when? Make or buy? How fast can a manufacturing set-up project finish? | EOQ, reorder point, production-run model, PERT/CPM, project crashing | Order 20 units, 5 times a year, reorder at 7 units (21 if lead time triples); keep buying rather than manufacturing; crash activity E for R4,000 to finish in 11 weeks |
| [03 Monte Carlo and Markov analysis](workbooks/03-monte-carlo-and-markov.xlsx) | What market share can we expect, and where does the market settle? | Monte Carlo simulation (20 trials), Markov chains, steady-state analysis | Simulated share 74.5% now, settling at 52.9% against competitors at 29.4% and 17.6%: keep the business but plan for declining share |

## Markov steady state in Python

[`python/markov_steady_state.py`](python/markov_steady_state.py) re-solves the Excel model, π = πP with the shares summing to 1. It confirms the steady state of 0.529 / 0.294 / 0.176. The market settles within about 10–14 periods, depending on the tolerance used.

```bash
pip install numpy
python python/markov_steady_state.py
```

## Related work

Honours Decision Support Systems (ITRI618/628, 2026) extended this with linear programming and transportation models in Excel Solver, such as shipping-route cost minimisation with sensitivity analysis on removed routes.
