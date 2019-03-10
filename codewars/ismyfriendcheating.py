from itertools import combinations as cb

def removNb(n):
    l = []
    possible_a_b = list(cb(range(1,n+1),2))
    
    for i,j in possible_a_b:
        if i * j == sum([num for num in range(n+1) if num != i and num != j]):
            l.append((i,j))
            l.append((j,i))

    return l


def original_removNb(n):
    l = []
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            if i * j == sum([num for num in range(n+1) if num != i and num != j]):
                l.append((i,j))
                l.append((j,i))

    return l




# test.assert_equals(removNb(100), [])
# test.assert_equals(removNb(26), [(15, 21), (21, 15)])
# test.assert_equals(removNb(210), [(115, 190), (190, 115)])