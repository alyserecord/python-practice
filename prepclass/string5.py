# Example input() statement
s = str(input('Please enter a string: '))

if s.endswith('!!!'):
    s = s.replace('!!!', '.')

# Print the string when you are done
print(s)