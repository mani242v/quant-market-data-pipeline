import subprocess

print("Starting Quant Market Data Pipeline...\n")

print("Step 1: Fetching market data...")
subprocess.run(["python", "fetch_market_data.py"])

print("\nStep 2: Processing data...")
subprocess.run(["python", "process_market_data.py"])

print("\nStep 3: Loading data into Snowflake...")
subprocess.run(["python", "load_to_snowflake.py"])

print("\nPipeline execution completed successfully.")