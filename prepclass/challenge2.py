#Write a script that computes the factorial of a user-inputted 
#positive number and prints the result.

number = int(input('Please enter a number: '))
result = 1

while number > 0:
    result *= number
    number -= 1
print(result)