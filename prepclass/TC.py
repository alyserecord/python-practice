# Write a script that prompts the user to input a series of numbers 
# separated by commas. Your script will then take these inputted 
# numbers and store them as a list of tuples, two at a time. 
# Finally, your script will print that list of tuples to the user. 
# If the user inputs an odd number of numbers, then only make a 
# list of the largest number of pairs of two that are possible.

# Example: If you inputted the numbers 1, 2, 3, 4, 5, 6, your 
# script should print [(1, 2), (3, 4), (5, 6)]. 
# If you inputted the numbers 1, 2, 3, 4, 5, your script should 
# print [(1, 2), (3, 4)].

l = input('enter a comma separated list of numbers: ')

zipped = zip((int(item) for item in l.split(',')[::2]), (int(item) for item in l.split(',')[1::2]))

result = [item for item in zipped]

print(result)
