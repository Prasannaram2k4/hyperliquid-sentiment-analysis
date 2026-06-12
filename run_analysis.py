import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as plt_sns
import os
import json

trader_file = "hyperliquid_trader_data.csv"
sentiment_file = "bitcoin_sentiment.csv"
output_dir = "plots"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# 1. Data Preprocessing & Merging
print("Loading data...")
try:
    df_trader = pd.read_csv(trader_file)
    df_sentiment = pd.read_csv(sentiment_file)
except FileNotFoundError:
    print("Datasets not found. Please run `python download_and_explore.py` first.")
    exit(1)

# Convert Trader Timestamp to Date
print("Converting timestamps...")
# The Timestamp is in milliseconds
df_trader['Datetime'] = pd.to_datetime(df_trader['Timestamp'], unit='ms')
df_trader['date'] = df_trader['Datetime'].dt.strftime('%Y-%m-%d')

# Merge Datasets
print("Merging datasets...")
df_merged = pd.merge(df_trader, df_sentiment, on='date', how='inner')

print(f"Merged Data Shape: {df_merged.shape}")

# Add Win/Loss Column
df_merged['Is Win'] = df_merged['Closed PnL'] > 0

# 2. EDA
print("Generating plots...")
plt_sns.set_theme(style="whitegrid")

# PnL by Sentiment
plt.figure(figsize=(10, 6))
plt_sns.boxplot(data=df_merged, x='classification', y='Closed PnL', showfliers=False)
plt.title('PnL Distribution by Market Sentiment (Excluding Outliers)')
plt.savefig(os.path.join(output_dir, "pnl_by_sentiment.png"))
plt.close()

# Trading Volume by Sentiment
volume_by_sentiment = df_merged.groupby('classification')['Size USD'].sum().reset_index()
plt.figure(figsize=(10, 6))
plt_sns.barplot(data=volume_by_sentiment, x='classification', y='Size USD')
plt.title('Total Trading Volume by Sentiment Classification')
plt.savefig(os.path.join(output_dir, "volume_by_sentiment.png"))
plt.close()

# 3. In-Depth Analysis
print("Calculating metrics...")
# Win Rate and Avg PnL by Sentiment
metrics = df_merged.groupby('classification').agg(
    Trade_Count=('Closed PnL', 'count'),
    Avg_PnL=('Closed PnL', 'mean'),
    Total_PnL=('Closed PnL', 'sum'),
    Win_Rate=('Is Win', 'mean'),
    Avg_Size_USD=('Size USD', 'mean')
).reset_index()

# Win Rate by Sentiment and Direction
metrics_dir = df_merged.groupby(['classification', 'Direction']).agg(
    Trade_Count=('Closed PnL', 'count'),
    Win_Rate=('Is Win', 'mean'),
    Avg_PnL=('Closed PnL', 'mean')
).reset_index()

# Save metrics to JSON for the report
output_data = {
    "total_trades": len(df_merged),
    "overall_win_rate": float(df_merged['Is Win'].mean()),
    "sentiment_metrics": metrics.to_dict('records'),
    "direction_metrics": metrics_dir.to_dict('records')
}

with open("metrics.json", "w") as f:
    json.dump(output_data, f, indent=4)

# Directional Win Rate Plot
plt.figure(figsize=(12, 6))
plt_sns.barplot(data=metrics_dir, x='classification', y='Win_Rate', hue='Direction')
plt.title('Win Rate by Sentiment and Trade Direction')
plt.savefig(os.path.join(output_dir, "winrate_direction_sentiment.png"))
plt.close()

print("Analysis script finished successfully. Plots saved to 'plots/' directory.")
