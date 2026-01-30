# Binance Futures Testnet Trading Bot (Python)

A simple CLI-based trading bot built in Python that places orders on **Binance Futures Testnet (USDT-M)**.  
This project demonstrates clean code structure, API integration, input validation, logging, and error handling.

> ⚠️ This bot uses **Binance Futures Testnet** only. No real funds are involved.

---

## Features

- Place **MARKET** and **LIMIT** orders
- Supports **BUY** and **SELL**
- Command-line interface (CLI)
- Input validation with clear error messages
- Structured, reusable codebase
- Detailed logging of API requests, responses, and errors
- Exception handling for API and network errors

---

## Tech Stack

- Python 3.x
- [python-binance](https://github.com/sammchardy/python-binance)
- argparse
- logging

---

## Project Structure
- trading_bot/
- ├── bot/
- │ ├── init.py
- │ ├── client.py # Binance Futures client wrapper
- │ ├── orders.py # Order placement logic
- │ ├── validators.py # CLI input validation
- │ └── logging_config.py # Logging configuration
- ├── cli.py # CLI entry point
- ├── logs/
- │ └── bot.log # API request/response logs
- ├── requirements.txt
- ├── README.md
- └── .env

---

## Install Dependencies
pip install -r requirements.txt

---

## Configure Environment Variables
- BINANCE_API_KEY=your_api_key_here
- BINANCE_API_SECRET=your_api_secret_here

---

# Sample Input

## Market Buy
- python cli.py \
-   --symbol BTCUSDT \
-   --side BUY \
-   --type MARKET \
-   --quantity 0.002

## Market Sell
- python cli.py \
-   --symbol BTCUSDT \
-   --side SELL \
-   --type MARKET \
-   --quantity 0.002

## Limit Buy
- python cli.py \
-   --symbol BTCUSDT \
-   --side BUY \
-   --type LIMIT \
-   --quantity 0.002 \
-   --price 75000


## Limit Sell
- python cli.py \
-   --symbol BTCUSDT \
-   --side SELL \
-   --type LIMIT \
-   --quantity 0.002 \
-   --price 80000

---

# Example CLI Output
- Order placed successfully
- Order ID: 12345678
- Status: FILLED
- Executed Qty: 0.002
- Avg Price: 78120.5
