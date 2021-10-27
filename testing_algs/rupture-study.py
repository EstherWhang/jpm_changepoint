import scipy.stats as stats
import matplotlib.pyplot as plt
import ruptures as rpt

# importing the sys module
import sys        
  
# inserting the mod.py directory at 
# position 1 in sys.path
#SET UP INIT, for now update this for your path
sys.path.insert(1, r'C:\Users\emw\Desktop\Cooper\Junior\breakthroughAI_jpmorgan\jpm_changepoint')  
from modules.gener import *
from modules.utilities import *
from modules.gauss_mixture import *


#first: trying to break current dectectors: 
gen1 = ChangingDistributionGenerator(stats.norm, {"loc":4,"scale":1}, stats.norm, {"loc":10,"scale":3},25)
vals = np.zeros(100)
for i in range(100):
    vals[i] = gen1.get()
# piecewise constant data 
n_samples, n_dims, sigma = 100, 1, 5
n_bkps = 4  # number of breakpoints
signal_c, bkps_c = rpt.pw_constant(n_samples, n_dims, n_bkps, noise_std=sigma)


#mu_true = np.array([-1, 0, 1])
#sigma_true = np.sqrt([0.3, 0.1, 0.25])
#mixture_p = [0.3, 0.2, 0.5] 
#signal_mixed_gauss = sample_gauss_mix(mu_true, sigma_true, cluster_sizes)
print(bkps_c)
#print(bkps_c) # prints the breakpoint values, the start and end of the changepoint range
#fig, ax_array = rpt.display(signal_c, bkps_c)


#todo: make a bunch of synthetic time series datasets and test rupture algorithms on them
#Binary Segmentation (https://github.com/deepcharles/ruptures/blob/master/docs/user-guide/detection/binseg.md)
#Bottom-up segmentation (https://github.com/deepcharles/ruptures/blob/master/docs/user-guide/detection/bottomup.md)
#Dynamic Programming (https://github.com/deepcharles/ruptures/blob/master/docs/user-guide/detection/dynp.md)
#Kernel change point detection (https://github.com/deepcharles/ruptures/blob/master/docs/user-guide/detection/kernelcpd.md)
#Linearly penalized segmentation (https://github.com/deepcharles/ruptures/blob/master/docs/user-guide/detection/pelt.md)
#Window-based change point detection (https://github.com/deepcharles/ruptures/blob/master/docs/user-guide/detection/window.md)

#one thing to do- check that the format of the data works with the rupture stuff as well
