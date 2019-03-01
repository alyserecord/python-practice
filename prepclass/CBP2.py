i = 1
total = 1

while i <= 20:
    if total > 1000000000:
        break
    total *= i
    i += 1
print (total)