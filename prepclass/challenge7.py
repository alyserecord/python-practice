number = int(input('Please enter a value for N: '))
result = 1
x = 1

while x <= number:
    result = (2 * result) + 1
    x += 1
print(result)