#https://blog.quantinsti.com/stock-market-data-analysis-python/
import yfinance as yf
import xlsxwriter as xl
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

start_date = '2021-10-01'
end_date = '2021-12-09'

# Setting tickers
tickers = 'AMZN'

# Downloading data
data = yf.download(tickers, start_date, end_date)

# Wrangling Data
data = data[['Adj Close']].round(2)
data = data.reset_index()
print(data)

# Visualization
# sns.set_theme()

sns.lineplot(data=data,
    x='Date', y='Adj Close'
)

plt.show()


# Writing to Excel
#data.to_excel('stock_overview.xlsx')