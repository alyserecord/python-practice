# Example input() statement
s = input('Please enter a string: ')

if len(s) < 2:
    # Use this error message if the string is too short
    print('String too short.')
else: 
    print(s[1::2])