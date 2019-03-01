#Write a script that computes the sum from 0 to a non-negative 
#inputted number and prints the result. This time though, 
#start at the user inputted number and work down to 0. 
#This answer will look very much like the example in the 
#lesson above; you'll just need to change a couple of things. 
#(Consider: What should the result be if the input is 0?)

user_num = int(input('Enter a number you idiot: '))
x = user_num
result = 0

while x <= user_num and x > 0:
    result += x
    x -= 1
print (result)