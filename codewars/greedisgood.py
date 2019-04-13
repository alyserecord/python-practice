def score(dice):
    # tally up the dice
    tally = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for item in dice:
        if item == 1:
            tally[1] += 1
        if item == 2:
            tally[2] += 1
        if item == 3:
            tally[3] += 1
        if item == 4:
            tally[4] += 1
        if item == 5:
            tally[5] += 1
        if item == 6:
            tally[6] += 1
    
    #assess the scores
    total = 0
    for x,y in tally.items():
        if y >= 3 and y <= 5:
            if x == 1:
                total += (x*1000)
            else:
                total += (x*100)
        elif y == 6:
            if x == 1:
                total += (x*2000)
            else:
                total += (x*200)
    if tally[1] >= 1 and tally[1] < 3:
        total += (tally[1] * 100)
    if tally[1] > 3 and tally[1] < 6:
        total += ((tally[1] - 3) * 100)
    if tally[5] >= 1 and tally[5] < 3:
        total += (tally[5] * 50)
    if tally[5] > 3 and tally[5] < 6:
        total += ((tally[5] - 3) * 50)

    return total