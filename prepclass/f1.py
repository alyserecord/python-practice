def get_divisors(n):
    '''
    This function calculates and returns all of the divisors of n,
    between 1 and n, inclusive.

    Parameters
    ----------
    n: {int}

    Returns
    -------
    divisors: {list} all divisors of n in order from smallest to
    largest
    '''
    result = []
    for item in range(1,n+1):
        if n % item == 0:
            result.append(item)
    result.sort()

    return result