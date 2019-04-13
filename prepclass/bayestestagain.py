def realpositive(TP,FP,perc_population):
    popwithout = 100 - perc_population
    return (perc_population * TP)/((perc_population * TP)+(popwithout * FP))