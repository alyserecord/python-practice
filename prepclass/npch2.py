import numpy as np

def mat_addition(A, B):
    """
    Add vector/matrix arrays A and B together. If they cannot be added
    return False.

    Parameters
    ----------
    A: NumPy array size of (n,) or (n, m)
    B: NumPy array size of (p,) or (p, q)

    Returns
    -------
    NumPy Array of same size as A and B, or False if their sizes differ.
    """
    if A.shape == B.shape:
        return A + B
    else: 
        return False