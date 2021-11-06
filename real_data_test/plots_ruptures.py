#functions for testing breakpoints with rupture
import ruptures as rpt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_company(company_stock, company_name, start, end):
    df = pd.read_csv("company_stock")
    df_range = df.loc[(df['Date'] >= start) & (df['Date'] < end)]
    df_range.plot(x='Date',y='Close')
    plt.title("company_name")
  
def bin_seg(signal, dates, model, sigma):
    #model = "l2"  # "l1", "rbf", "linear", "normal", "ar",...
    algo = rpt.Binseg(model=model).fit(signal)
    sigma = 5 #std of noise
    my_bkps = algo.predict(epsilon=3 * len(signal) * sigma ** 2)
    # show results
    print(dates[my_bkps[:-1]])
    rpt.show.display(signal, my_bkps, figsize=(10, 6))
    plt.title("Binary Segmentation")
    plt.show()
def bottom_up(signal, dates, model, sigma ):
  #model = "l2"  # "l1", "rbf", "linear", "normal", "ar",...
    algo = rpt.BottomUp(model=model).fit(signal)
    sigma = 5 #std of noise
    my_bkps = algo.predict(epsilon=3 * n * sigma ** 2)
  # show results
    print(dates[my_bkps[:-1]])
    rpt.show.display(signal, my_bkps, figsize=(10, 6))
    plt.title("Binary Segmentation")
    plt.show()
#models : "l2" linear, "rbf" gaussian
#Linearly penalized segmentation
#https://github.com/deepcharles/ruptures/blob/master/docs/examples/kernel-cpd-performance-comparison.ipynb
def pelt(signal, dates, model, jump=1, min_size=2,beta=100 ): #alternative to dynamic, linear kernal
    algo = rpt.Pelt(model=model, jump=jump, min_size=min_size).fit(signal)
    bkps = algo.predict(pen=beta)
    rpt.show.display(signal, bkps, figsize=(10, 6))
    plt.show()

def window(signal, dates, model):
    algo = rpt.Window(width=40, model=model).fit(signal)
    my_bkps = algo.predict(epsilon=3 * n * sigma ** 2)
    # show results
    rpt.show.display(signal, my_bkps, figsize=(10, 6))
    plt.show()