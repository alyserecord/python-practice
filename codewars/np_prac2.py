import numpy as np

def elements_greater_than_mean(arr):
    '''
    Return a new array with the elements of the array
    arr that are greater than its mean.

    >>> elements_greater_than_mean(np.array([0.2, 0.8, 0.3, 0.6]))
    array([0.8, 0.6])
    '''
    return arr[arr > np.mean(arr)]
