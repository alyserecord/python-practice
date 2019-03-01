def expanded_form(num):
    num_list = [int(x) for x in str(num)]
    num_list.reverse()
    expanded_nums = []
    for index, x in enumerate(num_list):
       if x > 0:
           expanded_nums.append(str(x * (10 ** index)))
    expanded_nums.reverse()
    return " + ".join(expanded_nums)