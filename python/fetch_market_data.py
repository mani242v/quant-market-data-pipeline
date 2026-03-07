import yfinance as yf
import pandas as pd
from datetime import datetime
import os

# Stocks to track
stocks = ["AAPL","MSFT","NVDA","AMZN","GOOGL","META","SPY","QQQ"]

print("Downloading market data...")

# Download 1 year of daily data
data = yf.download(stocks, period="1y", group_by="ticker")

all_data = []

for stock in stocks:
    df = data[stock].copy()
    df["symbol"] = stock
    df.reset_index(inplace=True)
    all_data.append(df)

final_df = pd.concat(all_data)

# Ensure raw folder exists
os.makedirs("../data/raw", exist_ok=True)

# Create timestamped file
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"../data/raw/market_data_{timestamp}.csv"

# Save file
final_df.to_csv(filename, index=False)

print("Data download complete.")
print("File saved:", filename)