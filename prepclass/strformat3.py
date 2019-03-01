from math import pi

# Example input() statement
n = int(input('Please enter an integer: '))

format_string = '{:.Nf}'
format_string = format_string.replace('N', str(n))

# Replace this with your own print statement
print(format_string.format(pi))