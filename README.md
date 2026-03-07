# Quant Market Data Pipeline

This project builds an automated financial market data pipeline that collects stock market data, processes technical indicators, and stores the results in Snowflake for analysis.

The pipeline can be executed manually or through GitHub Actions and updates market data for multiple assets.

---

## Architecture

The pipeline follows this flow:

Yahoo Finance API  
↓  
Python Data Ingestion  
↓  
Feature Engineering (Returns + Moving Averages)  
↓  
Snowflake Data Warehouse  
↓  
SQL Analytics & Strategy Signals

---

## Technologies Used

Python  
Pandas  
Snowflake  
SQL  
GitHub Actions  
Yahoo Finance API

---

## Tracked Assets

The pipeline currently collects data for the following assets:

AAPL  
MSFT  
NVDA  
AMZN  
META  
GOOGL  
SPY  
QQQ  

---

## Key Metrics Generated

The pipeline calculates several indicators used in financial analysis:

Daily Return  
20-Day Moving Average (MA20)  
50-Day Moving Average (MA50)  
Trading Signal based on Moving Average Crossover

Signal logic:

BUY → MA20 > MA50  
SELL → MA20 < MA50

---

## Project Structure
