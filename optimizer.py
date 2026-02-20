import yfinance as yf
import numpy as np
import pandas as pd
from scipy.optimize import minimize

def get_stock_data(tickers, period='2y'):
    data = yf.download(tickers, period=period, auto_adjust=True)
    if isinstance(data.columns, pd.MultiIndex):
        data = data['Close']
    else:
        data = data[['Close']]
        data.columns = tickers
    data = data.dropna()
    return data

def calculate_returns(data):
    returns = data.pct_change().dropna()
    mean_returns = returns.mean() * 252  # Annualised
    cov_matrix = returns.cov() * 252     # Annualised
    return mean_returns, cov_matrix

def portfolio_performance(weights, mean_returns, cov_matrix):
    ret = np.dot(weights, mean_returns)
    risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return ret, risk

def optimise_portfolio(tickers, risk_tolerance=0.5):
    data = get_stock_data(tickers)
    mean_returns, cov_matrix = calculate_returns(data)
    n = len(tickers)

    # Objective: maximise Sharpe ratio (return/risk)
    def neg_sharpe(weights):
        ret, risk = portfolio_performance(weights, mean_returns, cov_matrix)
        if risk == 0:
            return 0
        return -(ret / risk)

    constraints = {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}
    bounds = tuple((0, 1) for _ in range(n))
    initial = np.array([1/n] * n)

    result = minimize(neg_sharpe, initial, method='SLSQP',
                     bounds=bounds, constraints=constraints)

    weights = result.x
    ret, risk = portfolio_performance(weights, mean_returns, cov_matrix)

    return {
        'tickers': tickers,
        'weights': [round(w * 100, 2) for w in weights],
        'expected_return': round(ret * 100, 2),
        'risk': round(risk * 100, 2),
        'sharpe_ratio': round(ret / risk, 3) if risk > 0 else 0,
        'prices': data.iloc[-1].to_dict()
    }