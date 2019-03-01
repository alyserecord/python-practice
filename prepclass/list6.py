# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l = s.split(', ')
l.sort()

for idx, elem in enumerate(l,1):
    print (idx, elem)