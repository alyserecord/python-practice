# First get the string
s = input('Please enter a string: ')
s = s.upper()
# Then get the letter to count
l = input('Please enter a letter to count: ')
l = l.upper()
total = 0

for cool in s:
    if cool == l:
        total += 1

# Print the number of times letter is in the inputted string
print(total)