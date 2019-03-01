# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')

first = str(l[0])
l.append(first)
print(l)
# Append the first element to list l and then print the list