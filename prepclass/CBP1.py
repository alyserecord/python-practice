i = 1
total = 0

while i <= 20:
    if i % 3 == 0:
        i += 1
        continue
    total += i
    i += 1
print (total)