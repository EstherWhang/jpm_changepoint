#JPM Stock
import pandas as pd
import ruptures as rpt
import numpy as np
import matplotlib.pyplot as plt

JPMorgan_df = pd.read_csv("https://github.com/EstherWhang/jpm_changepoint/raw/main/JPM.csv")
print(JPMorgan_df.head())
JPMorgan = JPMorgan_df[['Date', 'Close','Volume']]
JPMorgan['Date'] = pd.to_datetime(JPMorgan['Date'], format='%Y-%m-%d')
JPMorgan_recent = JPMorgan.loc[(JPMorgan['Date'] >= '2020-01-1')]
JPMorgan_recent.plot(x='Date', y='Close')
plt.title('Closing vs Date from 2020-01-01 to 2020-04-01')
JPMorgan_recent.plot(x='Date', y='Volume')
plt.title('Volume vs Date from 2020-01-01 to 2020-04-01')
JPMorgan['Date'] = pd.to_datetime(JPMorgan['Date'], format='%Y-%m-%d')
JPMorgan_2008 = JPMorgan.loc[(JPMorgan['Date'] >= '2006-01-1') & (JPMorgan['Date'] < '2010-01-01')]
JPMorgan_2008.plot(x='Date', y='Close')
JPMorgan_2008.plot(x='Date', y='Volume')
JPMorgan['Date'] = pd.to_datetime(JPMorgan['Date'], format='%Y-%m-%d')
JPMorgan_interesting = JPMorgan.loc[(JPMorgan['Date'] >= '2010-01-1') & (JPMorgan['Date'] < '2015-01-01')]
JPMorgan_interesting.plot(x='Date', y='Close')
JPMorgan_interesting.plot(x='Date', y='Volume')