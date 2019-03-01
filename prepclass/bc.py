l1 = []
for x in range(7):
    y = int(input('Enter a num: '))
    l1.append(y)

l2 = []
for x2 in range(7):
    y2 = int(input('Enter a num: '))
    l2.append(y2)

common = []

for i in l1:
   if i in l2:
    common.append(i)

common.sort()


print(common)