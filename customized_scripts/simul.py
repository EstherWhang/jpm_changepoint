import matplotlib.pyplot as plt
import copy
from errorloss import *

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


