def calculate_ball_probability(red, green, purple, k):
    '''
    Calculate the probability that it takes k draws to match the
    ball drawn on draw zero

    Parameters
    ----------
    red: {int} Number of red balls
    green: {int} Number of green balls
    purple: {int} Number of purple balls
    k: {int} number of draw to calculate probability for

    Returns
    -------
    final_probability: {float} probability
    '''
    all = red + green + purple
    first_prob_red = red / all
    first_prob_green = green / all
    first_prob_purple = purple / all
    final_probability_red = 1
    final_probability_green = 1
    final_probability_purple = 1


    for x in (range(k-1)):
        red_running_prob = (green + purple - x)/(all - 1 - x)
        final_probability_red *= red_running_prob
        green_running_prob = (red + purple - x)/(all - 1 - x)
        final_probability_green *= green_running_prob
        purple_running_prob = (green + red - x)/(all - 1 - x)
        final_probability_purple *= purple_running_prob


    final_probability_red = final_probability_red * ((red-1)/(all - k)) * first_prob_red
    final_probability_green = final_probability_green * ((green-1)/(all - k)) * first_prob_green
    final_probability_purple = final_probability_purple * ((purple-1)/(all - k)) * first_prob_purple

    return final_probability_red + final_probability_purple + final_probability_green