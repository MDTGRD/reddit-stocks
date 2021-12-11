#https://medium.com/c%C3%B3digo-ecuador/how-to-scrape-yahoo-stock-price-history-with-python-b3612a64bdc6
import pandas as pd
import requests
from bs4 import BeautifulSoup

page  = requests.get("https://www.fool.com/investing/top-stocks-to-buy.aspx")

print(page)