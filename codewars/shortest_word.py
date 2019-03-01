def find_short(s):
    l = s.split()
    return min(l, key=len)