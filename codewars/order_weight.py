def order_weight(strng):
    wlist = strng.split(' ')
    t = 0
    summed = []
    final_list = []
    for item in wlist:
        for i in item:
            t += int(i)
        summed.append(t)
        t = 0
    a = list(zip(summed,wlist))
    new_a = sorted(a, key=lambda tup: (tup[0],tup[1]))
    for t2 in new_a:
        final_list.append(t2[1])
    return ' '.join(final_list)


#Test.assert_equals(order_weight("103 123 4444 99 2000"), "2000 103 123 4444 99")
#Test.assert_equals(order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"), "11 11 2000 10003 22 123 1234000 44444444 9999")
 #wlist = [int(item) for item in strng.split(' ')]