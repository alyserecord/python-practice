number = int(input('Please enter a number: '))
number2 = int(input('Please enter a another number: '))
result = min(number, number2)

while result > 0:
    if number % result == 0 and number2 % result == 0:
        print (result)
        break
    else:
        result -= 1