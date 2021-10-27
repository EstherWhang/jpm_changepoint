#mixture model setup

import numpy as np
from scipy.stats import norm
#Gaussian Mixture Proj 5
#setting up gaussian mixtures
#mu_true = np.array([-1, 0, 1])
#sigma_true = np.sqrt([0.3, 0.1, 0.25])
#mixture_p = [0.3, 0.2, 0.5] #how much of each distribution in mixutre

#z_0 is randomly selected value, the probability of getting z_0 from gauss mixture
def gauss_mix_dist(z_0, mu_true, sigma_true, mixture_p):
  #this makes the gaussian mixture
  p_1 = (mixture_p[0])*norm.pdf(z_0, mu_true[0], sigma_true[0]) 
  p_2 = (mixture_p[1])*norm.pdf(z_0, mu_true[1], sigma_true[1])
  p_3 = (mixture_p[2])*norm.pdf(z_0, mu_true[2], sigma_true[2])
  p_gauss_mix = p_1 + p_2 + p_3
  return p_gauss_mix

def sample_gauss_mix(k, mu_true, sigma_true, cluster_sizes):
#rejection sampling
  z = np.random.randn(1000)
  samples = []
  u = []
  index = []
  k = 3 #chose a number to scale normal to fit gaussian mixture, change it later
  for i , z_0 in enumerate(z):
    u_0 = np.random.random_sample()*k*norm.pdf(z_0, 0, 1)
    if u_0 <= gauss_mix_dist(z_0, mu_true, sigma_true, cluster_sizes):
      samples.append(z_0)
      u.append(u_0)
      index.append(i)
  return samples