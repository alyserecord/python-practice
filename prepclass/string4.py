# Example input() statement
s = str(input('Please enter a string: '))

if s.isupper():
    s = s.lower()
else:
    s = s.upper() + '!!!'

# Print the string when you are done
print(s)