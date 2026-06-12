import gdown
import pandas as pd
import os

# Google Drive File IDs
trader_data_id = "1IAfLZwu6rJzyWKgBToqwSmmVYU6VbjVs"
sentiment_data_id = "1PgQC0tO8XN-wqkNyghWc_-mnrYv_nhSf"

trader_file = "hyperliquid_trader_data.csv"
sentiment_file = "bitcoin_sentiment.csv"

# Download Trader Data
if not os.path.exists(trader_file):
    print("Downloading Trader Data...")
    gdown.download(id=trader_data_id, output=trader_file, quiet=False)
else:
    print("Trader Data already exists.")

# Download Sentiment Data
if not os.path.exists(sentiment_file):
    print("Downloading Sentiment Data...")
    gdown.download(id=sentiment_data_id, output=sentiment_file, quiet=False)
else:
    print("Sentiment Data already exists.")

print("\n--- Loading Trader Data ---")
try:
    df_trader = pd.read_csv(trader_file)
    print("Trader Data Shape:", df_trader.shape)
    print("Trader Data Columns:", df_trader.columns.tolist())
    print("\nTrader Data Info:")
    df_trader.info()
    print("\nTrader Data Head:")
    print(df_trader.head())
except Exception as e:
    print("Error loading trader data:", e)

print("\n--- Loading Sentiment Data ---")
try:
    df_sentiment = pd.read_csv(sentiment_file)
    print("Sentiment Data Shape:", df_sentiment.shape)
    print("Sentiment Data Columns:", df_sentiment.columns.tolist())
    print("\nSentiment Data Info:")
    df_sentiment.info()
    print("\nSentiment Data Head:")
    print(df_sentiment.head())
except Exception as e:
    print("Error loading sentiment data:", e)
