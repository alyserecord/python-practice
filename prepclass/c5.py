# Get the string
s = input('Please enter a string: ')
vowels = ['a', 'e', 'i', 'o', 'u']
newstring = s

for x in s:
    if x in vowels:
       newstring = newstring.replace(x,'')
print(newstring)