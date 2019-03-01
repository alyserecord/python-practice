#Write a script that takes two user inputted numbers and prints 
#"The first number is larger" or "The second number is larger" 
#depending on which is larger. If the numbers are equal, print 
#"The two numbers are equal". 

number = int(input('Please enter a number: '))
number2 = int(input('Please enter another number: '))

if number > number2:
    print('The first number is larger.')
elif number < number2:
    print('The second number is larger.')
else:
    print('The two numbers are equal.')