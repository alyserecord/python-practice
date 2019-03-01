nums = input('''Please enter a series of numbers separated by '-'. \n Hit enter when you are done. ''')

# input: 1 - 5 - 8 - 10
# output: {8: 64, 1: 1, 10: 100, 5: 25}

#nums.split('-')

my_dict = {int(num): int(num) ** 2 for num in nums.split('-')}

print (my_dict)