import math
import scipy.stats as stats
from collections import deque
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import copy
import random
from generator import *
from utilities import *


def r_squared_error_loss(target_point, stop_point):
    """
    Returns the root squared error loss when given the target point and stop point.
    target_point: The known point at which the signal changed.
    stop_point: The point at which the algorithm deteremined a stop should be performed.
    
    Returns: Root squared error loss between the two values.
    """
    return math.sqrt((target_point - stop_point) ** 2)

def root_mean_squared_error_loss(target_points, stop_points):
    """
    Returns the root mean squared error (RMSE) loss for a series of target values,
    and actual selected values.
    target_points: The known points at which the signal changed.
    stop_points: The points at which the algorithm deteremined a stop should be performed.
    
    Returns: Root mean squared error between the two sets.
    """
    cumulative_loss = 0.0
    for i in range(len(target_points)):
        cumulative_loss += (target_points[i] - stop_points[i]) ** 2
    return math.sqrt(cumulative_loss / (1.0 * len(target_points)))


class ChangeDetector(object):
    """
    The basic interface for our change detectors, it will be the responsibility
    of the simulator to check if the detector is triggered.
    """
    
    def __init__(self):
        self.triggered = False
        self.changepoint = 0
        self.count = 0
        self._previous = None
        
    def step(self, datum):
        """
        Performs all the necessary step action for a given detector,
        and incredibly naive approach to detecting change.
        
        Returns: True if change has been detected, False otherwise.
        """
        if self._previous is not None:
            if self._previous != datum:
                self.triggered = True
        self._previous = datum
        return self.triggered


    
class Simulator(object):
    """
    A basic simulator which takes a set of generator objects
    and a detector, running the detector against each generator
    once and recording the results.
    """
    
    def __init__(self, generators, detector, limit=1200):
        self._generators = generators
        self._detector = detector
        self._changepoints = []
        self._detected_changepoints = []
        self._limit = limit
        
        for generator in self._generators:
            self._changepoints.append(generator._changepoint)
            
    def plot(self, vals, changepoint, detected_changepoint, title):
        plt.plot(vals)
        plt.vlines(changepoint, max(vals) * 1.2, 1, color='black')
        plt.vlines(detected_changepoint, max(vals), 1, color='red')
        plt.title(title)
        plt.show()
        
    def run(self, plot=False):
        for generator in self._generators:
            detector = copy.deepcopy(self._detector)
            vals = []
            
            val = generator.get()
            changed = detector.step(val)
            vals.append(val)
            
            while not changed and len(vals) < self._limit:
                val = generator.get()
                vals.append(val)
                changed = detector.step(val)
            
            if changed:
                self._detected_changepoints.append(detector.changepoint)
            else:
                self._detected_changepoints.append(self._limit)
            
            if plot:
                self.plot(vals, generator._changepoint, detector.changepoint, generator.__class__.__name__)
        return root_mean_squared_error_loss(self._changepoints, self._detected_changepoints)



class ThreshDetector(object):
    
    def __init__(self, threshold=0.2, window_length=10, min_training=50):
        self._window = deque(maxlen=window_length)
        self._threshold = threshold
        self._triggered = False
        self.changepoint = 0
        self._min_training = min_training
        
        self._sum = 0
        self._sumsq = 0
        self._N = 0
        
    def step(self, datum):
        
        self._window.append(datum)
        
        # Welford's method
        self._N += 1
        self._sum += datum
        self._sumsq += datum ** 2
        
        self._mu = self._sum / self._N

        if self._N > self._min_training:
            variance = (self._sumsq - self._N * self._mu ** 2) / (self._N - 1)
            self._std = math.sqrt(variance)
            
            window_mu = sum(self._window) / len(self._window)
            ratio = window_mu / self._mu # TODO: Will fail if mu is zero.
            if ratio > (1.0 + self._threshold) or ratio < (1.0 - self._threshold):
                self._triggered = True
                self.changepoint = self._N
        return self._triggered


class WindowedMonteCarloDetector(ChangeDetector):
    
    def __init__(self, len1, len2, samples=1000, confidence=0.95, min_samples=50):
        self._window1 = deque(maxlen=len1)
        self._window2 = deque(maxlen=len2)
        self._confidence = confidence
        self._min_samples = min_samples
        self._samples = samples
        
        self._N = 0
        self._triggered = False
        self.changepoint = 0
        
        
    def step(self, datum):
        self._window1.append(datum)
        self._window2.append(datum)
        self._N += 1
        
        if self._N >= self._min_samples:
            diffs = np.zeros(self._samples)
            for i in range(self._samples):
                diffs[i] = random.choice(self._window1) - random.choice(self._window2)
            
            hdi_min, hdi_max = hdi(diffs, self._confidence)
            self._triggered = not between(0.0, hdi_min, hdi_max)
            if self._triggered:
                self.changepoint = self._N
        
        return self._triggered

