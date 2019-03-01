state = input('Please enter a State: ')

my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'Albany'}

print(my_dct.get(state,'Capitol not found'))

# check = False

# for element in my_dct:
#     if state == element:
#         answer = (my_dct[element])
#         check = True
#         break


# if check == True:
#     print (answer)
# else:
#     print('Capital not found!')