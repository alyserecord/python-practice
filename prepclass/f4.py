def next_perfect_square(number):
    import math
    '''
    Returns the next perfect square of the input number, 
    if the input numberis not a perfect square, returns -1.
    Ex:
    next_perfect_square(10)
    >>> -1
    next_perfect_square(9)
    >>> 16
    next_perfect_square(25)
    >>> 36
    next_perfect_square(37)
    >>> -1

    Parameters
    ----------
    number: {int}

    Returns
    -------
    next_perfect: {int} the next perfect square, or -1 if 
    number is not a perfect square
    '''
    if is_square(number) == True:
        for num in range(number+2,number + 100):
            if is_square(num) == True:
                return num
                break
    else:
        return -1