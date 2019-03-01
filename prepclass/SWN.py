#Write a script that prints the sum of the whole numbers 
#between 1 and a user inputted number.

user_num = int(input('Enter a number you idiot: '))
x = 1
result = 0

while x < user_num:
    if x > 1:
        result += x
    x += 1
print (result)