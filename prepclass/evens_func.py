def get_evens(n=5):
    evens = []
    for item in range(n):
        if item % 2 == 0:
            evens.append(item)
    return evens