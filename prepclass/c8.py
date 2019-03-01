# An empty list
l = []

# Get the numbers
n1 = int(input('Please enter a number: '))
n2 = int(input('Please enter a number to divide by: '))

for i in range(n1):
    if i % n2 == 0:
        l.append(i)

# Print the result
print(l)