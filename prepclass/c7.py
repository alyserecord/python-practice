# An empty list
l = []

# Get the number
n = int(input('Please enter a number: '))

for i in range (n):
    if i % 2 == 0:
        l.append(i)

# Print the result
print(l)