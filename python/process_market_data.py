import pandas as pd
import glob
import os

# Locate latest raw file
files = glob.glob("../data/raw/market_data_*.csv")
latest_file = max(files, key=os.path.getctime)

print("Processing file:", latest_file)

# Load data
df = pd.read_csv(latest_file)

# Convert date
df["Date"] = pd.to_datetime(df["Date"])

# Sort data
df = df.sort_values(["symbol", "Date"])

# Calculate daily return
df["daily_return"] = (df["Close"] - df["Open"]) / df["Open"]

# Moving averages
df["MA20"] = df.groupby("symbol")["Close"].transform(lambda x: x.rolling(20).mean())
df["MA50"] = df.groupby("symbol")["Close"].transform(lambda x: x.rolling(50).mean())

# Trading signal
df["signal"] = "HOLD"
df.loc[df["MA20"] > df["MA50"], "signal"] = "BUY"
df.loc[df["MA20"] < df["MA50"], "signal"] = "SELL"

# Ensure processed folder exists
os.makedirs("../data/processed", exist_ok=True)

# Save processed data
output_file = "../data/processed/processed_market_data.csv"
df = df[
    [
        "Date",
        "symbol",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "daily_return",
        "MA20",
        "MA50",
        "signal",
    ]
]
df.to_csv(output_file, index=False)

print("Processing complete.")
print("File saved:", output_file)