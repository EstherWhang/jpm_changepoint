import math
from collections import deque
import numpy as np
import random
from gener import *
from utilities import *
from errorloss import *

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

