#JPM Stock
import pandas as pd
import ruptures as rpt
import numpy as np
import matplotlib.pyplot as plt

from modules.plots_ruptures import *

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
print("-----------------------------------------------")
print("---------------Known Break Point---------------")
bin_seg(signal, dates, model)
bottom_up(signal, dates, model)
dyn_p(signal, dates, model)
window(signal, dates, model)

print("-----------------------------------------------")
print("--------------Unknown Break Point--------------")
#note: since there is no artificial breakpoint, color change is the rupture's prediction
bin_seg(signal, dates, model, changepoint_num = 0)
bottom_up(signal, dates, model,  changepoint_num = 0)
pelt(signal, dates, model) 
window(signal, dates, model,  changepoint_num = 0)
""" 
Known Break Point
Binary Seg Breaks: ['2020-03-03']
Bottom Up Breaks: ['2020-03-10']
Dynamic Programming: ['2020-03-03']
Window Breaks: ['2020-03-10']
Unknown Break Point
Binary Seg Breaks: ['2020-03-03']
Bottom Up Breaks: ['2020-03-10']
PELT: ['2020-02-25' '2020-03-05' '2020-03-09' '2020-03-18' '2020-03-24']
Window Breaks: ['2020-02-25' '2020-03-10']
"""