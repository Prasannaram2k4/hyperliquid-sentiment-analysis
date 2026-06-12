# Hyperliquid Trader Performance vs. Market Sentiment

This repository contains a comprehensive data science analysis exploring the relationship between trader performance on [Hyperliquid](https://hyperliquid.xyz/) and overall Bitcoin market sentiment (Fear & Greed Index). 

The goal of this project is to uncover hidden trading patterns, identify periods of optimal profitability, and deliver actionable insights for smarter trading strategies.

---

## 📊 Walkthrough & Key Findings

We have successfully processed and analyzed the historical trader data against the Bitcoin Market Sentiment index. Here is a summary of the approach, the key findings, and actionable insights.

### What Was Completed
1. **Data Preprocessing & Merging**: 
   - Converted the timestamp from the raw trades dataset into a standard datetime format.
   - Merged the dataset with the Bitcoin sentiment index ensuring accurate date alignment. This resulted in over **184,000 viable matched trades**.
2. **Exploratory Data Analysis (EDA)**: 
   - Examined PnL distribution across sentiment tiers (Fear, Extreme Greed, etc.).
   - Visualized trading volume by sentiment classification.
3. **In-Depth Metric Generation**: 
   - Calculated Win Rates, Trade Counts, and Average PnL per trade broken down by sentiment class and trade direction.

### 1. Market Activity Heavily Skews Toward "Fear"
A staggering majority of trading activity occurred during "Fear" periods. 
- **Fear**: ~133,000 trades 
- **Greed**: ~36,000 trades
- **Extreme Greed**: ~6,900 trades
- **Neutral**: ~7,100 trades

![Volume by Sentiment](plots/volume_by_sentiment.png)

> **Insight:** Traders are highly active when the market is fearful. This could represent a mix of panic selling and smart-money accumulation.

### 2. Profitability Shifts with Sentiment
While Fear periods see the most volume, the **Win Rate is highest during Extreme Greed (49.0%)** compared to Fear (41.5%) and Neutral (31.7%).

However, the **Average PnL per Trade is highest during standard "Greed" ($87.89)**, dropping to $50.04 in "Fear" and $25.41 in "Extreme Greed".

![PnL Distribution](plots/pnl_by_sentiment.png)

> **Actionable Strategy:** The data suggests that riding the trend during standard "Greed" phases is the most lucrative in terms of average payout, but "Extreme Greed" sees the highest probability of winning a trade (though with smaller relative returns).

### 3. Directional Success Varies Greatly
When analyzing specific trade directions (Open Long, Close Long, Open Short, Close Short):
- Closing a Long position during "Fear" yields a massive ~88% win rate and $72.20 Avg PnL, highlighting successful capitulation buying or securing profits early during drawdowns.
- Shorting behavior (Close Short) also thrives during Fear ($189 Avg PnL), confirming the power of short-selling momentum during panics.
- Interestingly, selling behavior during "Greed" has an 86% win rate and an outstanding $270.71 Avg PnL.

![Win Rate by Direction](plots/winrate_direction_sentiment.png)

> **Actionable Strategy:** Traders systematically capture the most massive PnL upside by executing "Sells" and taking profits during the "Greed" phase, heavily outpacing typical Longs. 

### Conclusion & Next Steps
The statistical correlations found suggest that the Fear & Greed Index is a robust indicator to optimize positional sizing:
1. **Reduce Size in Neutral**: The lowest Win Rate (31.7%) and lowest Avg PnL occur during Neutral market phases. Avoiding chop is critical.
2. **Shorts in Fear, Sells in Greed**: The highest average PnL events come from cashing out ("Sell") during Greed and closing Shorts effectively during Fear.

---

## 🚀 Setup & Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/hyperliquid-sentiment-analysis.git
   cd hyperliquid-sentiment-analysis
   ```

2. Create a virtual environment and install the required dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## 📁 Datasets

Due to file size constraints, the raw datasets are not included in this repository. You can download them via the included script:

```bash
python download_and_explore.py
```

This will fetch:
- `hyperliquid_trader_data.csv` (Historical Hyperliquid Trades)
- `bitcoin_sentiment.csv` (Bitcoin Fear & Greed Index)

## 🧠 Running the Analysis

To execute the data processing, merging, and to generate the statistical visualizations locally in the `plots/` directory, run:

```bash
python run_analysis.py
```

## 📝 License

This project is open-source and available under the MIT License.
