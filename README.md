# Stock Portfolio Optimiser

## Overview
A web application that finds the optimal allocation of stocks in a portfolio 
using Markowitz Portfolio Theory. Given a list of stock symbols, the app 
fetches real historical data and calculates the allocation that maximises 
the Sharpe Ratio — the best possible return for the given level of risk.

## Features
- Real stock data fetched automatically via yfinance
- Markowitz Portfolio Optimisation using Scipy
- Sharpe Ratio maximisation
- Visual allocation bars per stock
- Optional investment amount for dollar allocation per stock
- Clean Flask web interface

## Technologies
Python, Flask, yfinance, NumPy, Pandas, Scipy

## How to Run
1. Install dependencies: `pip install flask yfinance pandas numpy scipy`
2. Run the app: `python app.py`
3. Open `http://127.0.0.1:5000` in your browser
4. Enter stock symbols separated by commas e.g. `AAPL, MSFT, TSLA`
5. Click Optimise
