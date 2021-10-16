# Utilities
import numpy as np


def calc_min_interval(x, alpha):
    """Internal method to determine the minimum interval of
    a given width"""

    # Initialize interval
    min_int = [None,None]

    try:

        # Number of elements in trace
        n = len(x)

        # Start at far left
        start, end = 0, int(n*(1-alpha))

        # Initialize minimum width to large value
        min_width = np.inf

        while end < n:

            # Endpoints of interval
            hi, lo = x[end], x[start]

            # Width of interval
            width = hi - lo

            # Check to see if width is narrower than minimum
            if width < min_width:
                min_width = width
                min_int = [lo, hi]

            # Increment endpoints
            start +=1
            end += 1

        return min_int

    except IndexError:
        print('Too few elements for interval calculation')
        return [None,None]


def hdi(trace, cred_mass=0.95):
    hdi_min, hdi_max = calc_min_interval(np.sort(trace), 1.0-cred_mass)
    return hdi_min, hdi_max

def between(val, minval, maxval):
    return val >= minval and val <= maxval