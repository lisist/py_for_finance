import datetime as dt
import pickle
import pandas as pd
import os
import pandas_datareader as web

### you need Dax tickers files such as Dax_tickers.picle
### refers to scarp_dax_tickers.py

with open('Dax_tickers.pickle','rb') as f:
    tickers = pickle.load(f)

def get_price_data(reload_tickers):

    start = dt.datetime(2005,1,1)
    end = dt.datetime(2018,12,31)

    if not os.path.exists('dax_dfs'):
        os.makedirs('dax_dfs')

    start = dt.datetime(2005, 1, 1)
    end = dt.datetime(2018, 12, 31)

    for ticker in reload_tickers:
        print(ticker)
        if not os.path.exists('dax_dfs/{}.csv'.format(ticker)):
            df = web.DataReader(ticker+".DE",'yahoo',start,end)
            df.to_csv('dax_dfs/{}-DE.csv'.format(ticker))
        else:
            print('Alread have {} '.format(ticker))
