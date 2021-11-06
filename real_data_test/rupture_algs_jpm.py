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


#known change point
bin_seg(signal, dates, model)
bottom_up(signal, dates, model)
dyn_p(signal, dates, model)
window(signal, dates, model)

#note: since there is no artificial breakpoint, color change is the rupture's prediction
bin_seg(signal, dates, model, changepoint_num = 0)
bottom_up(signal, dates, model,  changepoint_num = 0)
pelt(signal, dates, model) 
window(signal, dates, model,  changepoint_num = 0)
