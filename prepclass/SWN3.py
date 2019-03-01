#Write a script that takes a user inputted number and prints 
#whether it is positive, negative or zero, as 
#"The inputted number is (positive/negative/zero)", 
#depending in the input.

mynum = int(input('Enter a number: '))

if mynum / 1 > 0:
    print ('The inputted number is positive.')
elif mynum / 1 < 0:
    print ('The inputted number is negative.')
else:
    print ('The inputted number is zero.')