# Get the string
s = input('Please enter a string: ')

if s[-1] == "!":
    print(s.upper())
else:
    # Convert the string to upper or lowercase (as appropriate), and print it
    print(s.lower())