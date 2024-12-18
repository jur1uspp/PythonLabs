import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

# Обрати компанії для аналізу
companies = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']

# Завантажити дані акцій
data = {}
for company in companies:
    data[company] = yf.download(company, start='2010-01-01', end='2024-12-31')

# Розрахувати щоденні відсоткові зміни цін акцій
for company, df in data.items():
    df['Daily Returns'] = df['Close'].pct_change()

# Обчислити середню річну прибутковість та ризик (стандартне відхилення)
annual_returns = {}
for company, df in data.items():
    annual_returns[company] = df['Daily Returns'].mean() * 252  # assuming 252 trading days in a year
    std_dev = df['Daily Returns'].std() * np.sqrt(252)  # Annual standard deviation
    print(f"{company} - Annual Return: {annual_returns[company]}, Std Dev: {std_dev}")

# Візуалізація цін акцій з часом
plt.figure(figsize=(14, 7))
for company, df in data.items():
    plt.plot(df['Close'], label=company)

plt.title('Stock Prices Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Візуалізація прибутковості акцій
plt.figure(figsize=(14, 7))
for company, df in data.items():
    plt.plot(df['Daily Returns'], label=company)

plt.title('Daily Returns of Stocks')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.show()

# Портфельний аналіз
cov_matrix = pd.concat([df['Daily Returns'] for df in data.values()], axis=1).cov()
expected_returns = pd.DataFrame({company: df['Daily Returns'].mean() for company, df in data.items()}, index=[0])

# Власний портфель (задані пропорції)
# Наприклад, портфель з рівномірними вагами
weights = np.array([0.2, 0.2, 0.2, 0.2, 0.2])

# Очікувана прибутковість портфеля
portfolio_return = np.dot(weights, expected_returns.mean())

# Риск портфеля (стандартне відхилення)
portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

print(f"Portfolio Expected Return: {portfolio_return}")
print(f"Portfolio Risk: {portfolio_risk}")

# Побудова ефективної межі (efficient frontier)
num_portfolios = 1000
results = np.zeros((num_portfolios, 2))

for i in range(num_portfolios):
    weights = np.random.random(len(companies))
    weights /= np.sum(weights)
    returns = np.dot(weights, expected_returns.mean())
    risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    results[i, 0] = risk
    results[i, 1] = returns

# Візуалізація ефективної межі
plt.figure(figsize=(14, 7))
plt.scatter(results[:, 0], results[:, 1], c=results[:, 1] / results[:, 0], marker='o')
plt.title('Efficient Frontier')
plt.xlabel('Risk')
plt.ylabel('Return')
plt.show()
