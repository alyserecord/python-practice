number = int(input('Please enter a number: '))
number2 = int(input('Please enter a another number: '))
greaternum = max(number, number2)

while True:
    if ((greaternum % number == 0) and (greaternum % number2 == 0)):
        print (greaternum)
        break
    greaternum += 1