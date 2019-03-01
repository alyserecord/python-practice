# Write a script that prompts a user to input a list of words separated
# by commas, and then prints out the unique words in the list.

# Example: If you inputted the words 
# hello, there, how, are, you, hello, you, 
# your script would print how, you, there, hello, are.

words = input('Enter a list of comma separated words: ')

words_set = set(item for item in words.split(', '))
#words_list = [item for item in words_set]

sep = ', '

print(sep.join(words_set))