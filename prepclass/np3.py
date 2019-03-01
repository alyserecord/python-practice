import numpy as np


def mat_inner_product(X, Y):
    '''
    Multiply two numpy arrays, if possible.

    Parameters
    ----------
    X: array, shape (n, m)
    Y: array, shape (p, q)

    Returns
    -------
    ret: array, shape (n, q), or False
        If the two arrays cannot be multiplied (X times Y), then return False.
        Otherwise return the product.
    '''
    if X.shape[1] == Y.shape[0]:
        return X.dot(Y)
    else:
        return False
