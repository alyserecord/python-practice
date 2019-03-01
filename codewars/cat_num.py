def openOrSenior(data):
    # new_data = []
    # for item in data:
    #     if item[0] > 55 and item[1] > 7:
    #         new_data.append('Senior')
    #     else:
    #         new_data.append('Open')
    # return new_data

    return ['Senior' if item[0] > 55 and item[1] > 7 else 'Open' for item in data]

    # Hmmm.. Where to start?