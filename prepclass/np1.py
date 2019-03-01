import numpy as np

def elements_twice_min(arr):
    """
    Return all elements of array arr that are greater than or equal to 
    2 times the minimum element of arr.

    Parameters
    ----------
    arr: NumPy array (n, m)

    Returns
    -------
    NumPy Array, a vector of size between: 0 and (n * m) - 1
    """
    result = np.array([num for num in arr.flat if num > arr.min()*2])
    return result