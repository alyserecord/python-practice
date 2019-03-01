# Get the string
s = input('Please enter a string: ')
s2 = ''

for i, x in enumerate(s,1):
    if i % 2 == 0:
        s2 += x.upper()
    else:
        s2 += x.lower()    
print (s2)