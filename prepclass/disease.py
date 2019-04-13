def positive_test(TP, FP, perc_population):
    '''
    Parameters
    ----------
    TP: {float} true positive
        percentage of tests that99.5 were positive
        for the sample of subjects that had the disease
    FP: {float} false positive
        percentage of tests that were positive
        for the control population (disease-free subjects)

    percent_population : {float} percentage of the population that has the
    disease

    Returns
    -------
    {float} probability of having the disease for a person with a positive
    test resultru
    '''

    pophas = perc_population/100
    popdoesnt = 1 - pophas
    truepositive = TP/100
    falsepositive = FP/100
    result = (pophas * truepositive) / ((pophas * truepositive) + (popdoesnt * falsepositive))

    return result

    # perc_pos = (perc_population * TP) + ((100 - perc_population) * FP)
    # return ((perc_pos * perc_population) / perc_pos) / 100

    # return ((perc_population* TP)/((perc_population * TP)+((100 - perc_population) * FP)))/100


    # pophas = perc_population/100
    # popdoesnt = 1 - pophas
    # TP = TP/100
    # FP = FP/100
    # pr_p_actual = (pophas * TP)/((pophas * TP) + (FP * popdoesnt))
    # return (pr_p_actual*pophas)/TP