#https://blog.quantinsti.com/stock-market-data-analysis-python/
import yfinance as yf
import xlsxwriter as xl
import pandas as pd

start_date = '2020-03-01'
end_date = '2021-12-09'

# Setting tickers
tickers = 'AMZN'

data = yf.download(tickers, start_date, end_date)

data.to_excel('example1.xlsx')