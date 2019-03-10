from itertools import combinations as cb

def choose_best_sum(t, k, ls):
    all_sub_sum = [sum(item) for item in cb(ls, k)]
    return max([item for item in all_sub_sum if item <= t],default=None)

# def choose_best_sum_original(t, k, ls):
#     return max([item for item in sub_list(ls,k) if item <= t])

# def sub_list(ls, k):
#     sub_sum = []
#     for i in range(len(ls) + 1):
#         for j in range(i + 1,len(ls) + 1):
#             sub = ls[i:j]
#             if len(sub) <= k:
#                 sub_sum.append(sum(sub))
#     return sub_sum

# Test.it("Bigger numbers")
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# Test.assert_equals(choose_best_sum(230, 4, xs), 230)
# Test.assert_equals(choose_best_sum(430, 5, xs), 430)
# Test.assert_equals(choose_best_sum(430, 8, xs), None)