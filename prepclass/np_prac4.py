import numpy as np


def dot_product(a, b):
    '''
    Return the dot product of two numpy arrays of the same length.

    Parameters
    ----------
    a: numpy array with shape (n, )
        An array of floating point numbers.
    b: numpy array with shape (n, )
        An array of floating point numbers.

    Returns
    -------
    dot_prod: float
        The dot product of a and b.
    '''
    return np.sum(np.multiply(a,b))