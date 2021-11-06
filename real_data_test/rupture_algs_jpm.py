#JPM Stock
import pandas as pd
import ruptures as rpt
import numpy as np
import matplotlib.pyplot as plt
from plots_ruptures import *
#import data
JPMorgan_df = pd.read_csv("https://github.com/EstherWhang/jpm_changepoint/raw/main/JPM.csv")
print(JPMorgan_df.head())
JPMorgan_df = JPMorgan_df[['Date', 'Close','Volume']]
plot_close(JPMorgan_df, 'JP Morgan', '2020-01-01', '2020-04-01')

#run it through rupture algorithms
JPMorgan_recent = JPMorgan_df.loc[(JPMorgan_df['Date'] >= '2020-01-1')]
signal = np.array(JPMorgan_recent['Close'])
dates = np.array(JPMorgan_recent['Date'])
model = "l2"

bin_seg(signal, dates, model,sigma = 1)

bottom_up(signal, dates, model, sigma = 1)

pelt(signal, dates, model, jump=1, min_size=2,beta=100 )

window(signal, dates, model, sigma = 1)