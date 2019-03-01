number = int(input('Please enter a number: '))
x = (number - 1)
prime = True

while x > 1 :
    if number % x == 0: 
        prime = False
        break
    x -= 1
if prime == True and number != 1:
    print('The number you inputted is a prime number.')
else:   
    print('The number you inputted is not a prime number.')