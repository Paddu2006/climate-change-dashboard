# India Climate Change Dashboard

An interactive Streamlit dashboard tracking India's climate change indicators — temperature anomalies, rainfall patterns and extreme weather events from 1990 to 2023.

## Overview

Climate change data exists everywhere but remains inaccessible to most people. This project builds a single clear interactive dashboard that shows what is actually happening to India's climate — making complex data understandable for citizens, students and policymakers alike.

## What It Shows

| Indicator | Finding |
|-----------|---------|
| Temperature rise | +1.7°C since 1990 |
| Rainfall change | -18mm since 1990 |
| Extreme events 2023 | 19 events |
| Years covered | 34 years (1990-2023) |

## Dashboard Features

- Live temperature anomaly trend line
- Annual rainfall bar chart with colour scale
- Extreme weather events area chart
- State-wise temperature risk comparison
- Key metric cards at the top

## How to Run

```bash
git clone https://github.com/Paddu2006/climate-change-dashboard.git
cd climate-change-dashboard
pip install streamlit plotly pandas numpy
streamlit run dashboard.py
```

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| Streamlit | Web dashboard |
| Plotly | Interactive charts |
| Pandas | Data analysis |
| NumPy | Data generation |

## What I Learned
- How to build interactive web apps using Streamlit
- How to create interactive charts using Plotly
- How to display key metrics and multi-chart dashboards
- How climate indicators tell a clear story when visualised properly

## License
MIT License
