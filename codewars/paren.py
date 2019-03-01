def valid_parentheses(string):
    counter = 0
    for item in string:
        if item == '(':
            counter += 1
        elif item == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0 
    



    # list_str = [item for item in list(string) if item == '(' or item == ')']
    # if len(list_str) == 0:
    #     return True
    # else:
    #     if list_str.count('(') == list_str.count(')') and list_str[0]!=')' and list_str[-1]!='(':
    #         return True
    #     else:
    #         return False