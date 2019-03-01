number = int(input('Please enter a number: '))
x = 1

while x <= number: 
    if number % x == 0:
        print (x)
    x += 1