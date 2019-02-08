import bs4 as bs
import requests
import pickle
import pandas as pd

def dax_ticker_import():
    dt = requests.get('https://en.wikipedia.org/wiki/DAX').text
    soup = bs.BeautifulSoup(dt)
    tb = soup.find('table',{'class':'wikitable sortable'})

    tickers= []

    for row in tb.find_all('tr')[1:]:
        ticker = row.find_all('td')[3].text
        tickers.append(ticker)

    with open('Dax_tickers.pickle','wb') as f:
        pickle.dump(tickers,f)
