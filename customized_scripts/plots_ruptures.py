#functions for testing breakpoints with rupture
import ruptures as rpt
import matplotlib.pyplot as plt

def plot_close(df, company_name, start, end):
    df_range = df.loc[(df['Date'] >= start) & (df['Date'] < end)]
    df_range.plot(x='Date',y='Close')
    plt.title(company_name)
    plt.show()
  
def bin_seg(signal, dates, model, sigma = 5, changepoint_num = 1):
    #model = "l2"  # "l1", "rbf", "linear", "normal", "ar",...
    algo = rpt.Binseg(model=model).fit(signal)
    bkps = 0
    if changepoint_num  != 0: #we know the number of changepoints
      bkps = algo.predict(n_bkps=changepoint_num)
    else: #means we don't know how many changepoints there are
      bkps = algo.predict(epsilon=3 * len(signal) * sigma ** 2)
    # show results
    print("Binary Seg Breaks: "+ str(dates[bkps[:-1]]))
    rpt.show.display(signal, bkps)
    plt.title("Binary Segmentation")
    plt.show()

def bottom_up(signal, dates, model, sigma = 5,changepoint_num = 1):
  #model = "l2"  # "l1", "rbf", "linear", "normal", "ar",...
    algo = rpt.BottomUp(model=model).fit(signal)
    bkps = 0
    if changepoint_num  != 0: #we know the number of changepoints
      bkps = algo.predict(n_bkps=changepoint_num)
    else: #means we don't know how many changepoints there are
      bkps = algo.predict(epsilon=3 * len(signal) * sigma ** 2)

    bkps = algo.predict(epsilon=3 * len(signal) * sigma ** 2)
  # show results
    print("Bottom Up Breaks: "+ str(dates[bkps[:-1]]))
    rpt.show.display(signal, bkps)
    plt.title("Bottom-up segmentation")
    plt.show()

def dyn_p(signal, dates, model, changepoint_num = 1): #number of changepoints are known
      # change point detection
    algo = rpt.Dynp(model=model, min_size=3, jump=5).fit(signal)
    bkps = algo.predict(n_bkps=changepoint_num )
    print("Dynamic Programming: "+ str(dates[bkps[:-1]]))
# show results
    rpt.show.display(signal, bkps)
    plt.title("Dynamic Programming")
    plt.show()


#models : "l2" linear, "rbf" gaussian
#Linearly penalized segmentation
#https://github.com/deepcharles/ruptures/blob/master/docs/examples/kernel-cpd-performance-comparison.ipynb
def pelt(signal, dates, model, jump=1, min_size=2,beta=100 ): 
  #alternative to dynamic, when you don't know number of changepoints
    algo = rpt.Pelt(model=model, jump=jump, min_size=min_size).fit(signal)
    bkps = algo.predict(pen=beta)
    print("PELT: "+ str(dates[bkps[:-1]]))
    rpt.show.display(signal, bkps)
    plt.title("Linearly penalized segmentation")
    plt.show()

def window(signal, dates, model, sigma = 5, changepoint_num = 1):
    algo = rpt.Window(width=10, model=model).fit(signal)
    bkps = 0
    if changepoint_num != 0: #we know the number of changepoints
      bkps = algo.predict(n_bkps=changepoint_num)
    else: #means we don't know how many changepoints there are
      bkps = algo.predict(epsilon=3 * len(signal) * sigma ** 2)
    # show results
    print("Window Breaks: "+ str(dates[bkps[:-1]]))
    rpt.show.display(signal, bkps)
    plt.title("Window-based change point detection")
    plt.show()