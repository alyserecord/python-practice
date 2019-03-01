# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')

print(l[1::2])

# Print the odd-indexed elements of list l