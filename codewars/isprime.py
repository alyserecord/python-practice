def is_prime(num):
    prime_check = True
    if num > 2:
        for item in range(2,num):
            if num % item == 0:
                prime_check = False
    if num < 2:
        prime_check = False
    return prime_check
