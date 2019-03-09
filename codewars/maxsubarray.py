def maxSequence(arr):
    return max([sum(item) for item in sub_lists(arr)])
#find all sub lists
def sub_lists(arr):
    sub_list = [[]]
    for i in range(len(arr)+1):
        for j in range(i + 1, len(arr)+1):
            sub = arr[i:j]
            sub_list.append(sub)
    return sub_list


            


# test.describe("Tests")
# test.it('should work on an empty array')   
# test.assert_equals(maxSequence([]), 0)
# test.it('should work on the example')
# test.assert_equals(maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)