def is_prime(n):
    '''
    Return True if the input is prime, False otherwise
    Parameters
    ----------
    n: {int} input integer

    Returns
    -------
    is_prime: {bool} whether n is prime
    '''
    prime_check = True

    for num in range (2,n):
        if n % num == 0:
            prime_check = False

    return prime_check