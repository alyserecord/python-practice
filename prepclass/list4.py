# Input series of comma-separated strings
s = input('Please enter a series of comma-separated strings: ')
# Split on comma+space to create the list
l1 = s.split(', ')
l2 = list(l1)
l2.reverse()
l2.pop(0)

l3 = l1 + l2
print(l3)

# Convert list l into a palindrome and then print the list