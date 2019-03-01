def count_pair_sums(arr, number=0):
    '''
    Given an array, find the count of how many pairs of numbers in 
    the array sum to the input number

    Parameters
    ----------
    arr: {list} list of integers (positive and negative)
    number: number to see if pairs sum to (default 0)

    Returns
    -------
    {int} the number of pairs found that sum to given number
    '''

    # count_pair_sums([7, 7, 8, 8], 15) answer: 4
    # count_pair_sums([1, 1, 1, 1], 2) answer: 6
    # count_pair_sums([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11) answer: 9


    counter = 0
    index_array = []

    for index1, item1 in enumerate(arr):
        for index2, item2 in enumerate(arr):
            if index1 != index2:
                if item1 + item2 == number:
                    maybe_set = {index1, index2}
                    if maybe_set in index_array:
                        continue
                    else:
                        counter += 1
                        index_array.append(maybe_set)
    return counter




# let indexArray = [[0,1], [0, 2], [0, 3], [1, 2], [1, 3]]
#     for index1, item1 in enumerate(arr) {
#         for index2, item2 in enumerate(arr) {
#             if index1 != index2 {
#                 if item1 + item2 == number {
#                     // store index pair as a set in an array (array 
#                     of sets)
#                     // iterate through that array to see 
#                     if a set of the indexes already exist, 
#                     and conintue if the indexes have already been
#                     compared
#                     if !indexArray.contains([index1, index2]) {
#                         continue
#                     } else {
#                         count++
#                     }
#                 }
#             }
#         }
#     }


    # while running:
    #     for i in arr:    
    #         for index, item in enumerate(arr):
    #             item1 = item
    #             item2 = arr[(index + 1) % len(arr)]
    #             if item1 + item2 == number:
    #                 counter += 1
    #         arr.remove(i)
    #     break
    
    # return counter