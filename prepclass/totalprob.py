import numpy as np

def LawOfTotalProbability(conditional_probabilities, marginal_probabilities):
    '''
    Calculate the marginal probability of Pr(E_1) using the law of total probability
    when you are given numpy arrays of the conditional and marginal probabilities

    Return "Two equal length numpy arrays only" if the arrays are not equal length
    Return "The marginal probabilities do not sum to 1" if the marginal probabilities
    do not sum to one.
    
    Parameters
    ----------
    conditional_probabilities : {numpy array} 
        [Pr(E_1|F_1), Pr(E_1|F_2), ..., Pr(E_1|F_m)]
    marginal_probabilities : {numpy array} [Pr(F_1), Pr(F_2), ..., Pr(F_m)]

    Returns
    -------
    {float} probability of E_1 or {str} invalid input message
    
    Example:
    >>> LawOfTotalProbability(np.array([0.4, 0.03]), np.array([0.02, 0.98]))
    0.0374
    '''

    if len(conditional_probabilities) != len(marginal_probabilities):
        return "Two equal length numpy arrays only"

    elif sum(marginal_probabilities) != 1:
        return "The marginal probabilities do not sum to 1"

    else:
        return sum(conditional_probabilities *  marginal_probabilities)

print (LawOfTotalProbability(np.array([0.4, 0.03]), np.array([0.02, 0.98])))