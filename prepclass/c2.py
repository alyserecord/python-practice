# Example input() statement
number = int(input('Please enter a number: '))
isprime = True

# Here are the print statements that you should use.
for num in range(2, number):
    if number % num == 0:
        isprime = False
if isprime == True and number != 0:
    print ('The number you inputted is a prime number.')
else:
    print('The number you inputted is not a prime number.')