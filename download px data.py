import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

#start = dt.datetime(2010,1,1)
#end = dt.datetime(2016,12,31)
#tsla = web.DataReader('TSLA','yahoo',start,end)
#tsla.to_csv('tsla.csv')

style.use('ggplot')
tsla = pd.read_csv('tsla.csv',parse_dates=True,index_col=0)
tsla['100ma'] = tsla['Adj Close'].rolling(window=100,min_periods=0).mean()

tsla_ohlc = tsla['Adj Close'].resample('10D').ohlc()
tsla_vol = tsla['Volume'].resample('10D').sum()
print(tsla_vol.head())

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(5,0),rowspan=1,colspan=1, sharex=ax1)

ax1.plot(tsla_ohlc.index,tsla_ohlc['close'])
ax2.plot(tsla_vol.index,tsla_vol)
plt.show()
