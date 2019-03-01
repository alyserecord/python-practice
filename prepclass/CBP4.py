# Use the variables row and col. You will want to initialize them differently.
row, col = 0, 1

while row <= 3:
    row += 1
    while col <= 3: 
        if col == row:
            col += 1        
        if col == 4 or row == 4:
            break
        print (row, col)
        col += 1
    col = 1
        


# Use this print statement within your inner loop
#print(row, col)