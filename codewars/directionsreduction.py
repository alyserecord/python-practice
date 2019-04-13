def dirReduc1(arr):
    ns_counter = 0
    for i in arr:
        if i == "NORTH":
            ns_counter += 1
        elif i == "SOUTH":
            ns_counter -= 1

    ew_counter = 0
    for i in arr:
        if i == "EAST":
            ew_counter += 1
        elif i == "WEST":
            ew_counter -= 1

    norths = ["NORTH" for item in range(ns_counter) if ns_counter > 0]
    souths =  ["SOUTH" for item in range(abs(ns_counter)) if ns_counter < 0]
    easts = ["EAST" for item in range(ew_counter) if ew_counter > 0]
    wests = ["WEST" for item in range(abs(ew_counter)) if ew_counter < 0]
    answer = norths + souths + wests + easts

    return answer

def dirReduc(arr):
    combo1 = ['NORTH','SOUTH']
    combo2 = ['SOUTH','NORTH']
    combo3 = ['WEST','EAST']
    combo4 = ['EAST','WEST']
    final_arr = arr
    
    for item in arr[:-1]:
        for item2 in arr[1:]:
            if [item, item2] == combo1 or [item, item2] == combo2 or [item, item2] == combo3 or [item, item2] == combo4:
                final_arr.remove(item)
                final_arr.remove(item2)
    return final_arr

print (dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# test.assert_equals(dirReduc(a), ['WEST'])
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
# test.assert_equals(dirReduc(u), ["NORTH", "WEST", "SOUTH", "EAST"])