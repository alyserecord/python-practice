def spin_words(sentence):
    new_list = []
    for item in sentence.split():
        if len(item) > 4:
            new_item = ""
            for i in item:
                new_item = i + new_item
            new_list.append(new_item)
        else:
            new_list.append(item)
    return " ".join(new_list)
        
    #return " ".join(item for item in sentence.split(' '))