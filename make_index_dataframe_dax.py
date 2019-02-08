import pandas as pd
import pickle

### You need to have dax tickers
### refers to scarp_dax_tickers.py

### You need to have price data files for the index dataframe
### refers to get_price_data_for_dax.py

with open('Dax_tickers.pickle','rb') as f:
    tickers = pickle.load(f)

def make_index_dataframe(tickers):

    df_main = pd.DataFrame()

    for ticker in tickers:
        df = pd.read_csv('dax_dfs/{}-DE.csv'.format(ticker))
        df.set_index('Date',inplace=True)
        df.rename(columns = {'Adj Close':ticker},inplace=True)
        df.drop(['High','Low','Open','Close','Volume'],'columns',inplace=True)

        if df_main.empty:
            df_main = df
        else:
            df_main = df_main.join(df,how='outer')

    return df_main

make_index_dataframe(tickers).to_csv("dax_index.csv")
