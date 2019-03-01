import numpy as np

def mat_rank(X):
    """
    Given a matrix X, return its rank.

    Parameters
    ----------
    X: NumPy array size of (n, m)

    Returns
    -------
    (int) the rank of X
    """
    return np.linalg.matrix_rank(X)