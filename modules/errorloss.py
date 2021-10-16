import math
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

