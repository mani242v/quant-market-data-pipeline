import snowflake.connector
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

# Path to processed dataset
file_path = "../data/processed/processed_market_data.csv"

# Load dataset
df = pd.read_csv(file_path)

# Remove rows with missing moving averages
df = df.dropna(subset=["MA20","MA50"])

# Match Snowflake column names
df.columns = [c.upper() for c in df.columns]

# Reset index
df = df.reset_index(drop=True)

print("Connecting to Snowflake...")

conn = snowflake.connector.connect(
    user="mani120",
    password="Manikanta@24Vakkapatla",
    account="JGB83280",
    warehouse="MARKET_WH",
    database="QUANT_MARKET_DB",
    schema="MARKET_DATA"
)

print("Connected to Snowflake.")

success, nchunks, nrows, _ = write_pandas(
    conn,
    df,
    table_name="STOCK_PRICES"
)

if success:
    print(f"Uploaded {nrows} rows successfully.")
else:
    print("Upload failed.")

conn.close()