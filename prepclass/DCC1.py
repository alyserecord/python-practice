words = input('Enter words to transform to uppercase here. Separate them with spaces:')

word_list = words.split()

result = {word: word.upper() for word in word_list}

print(result)

#{'organic': 'ORGANIC', 'kale': 'KALE', 
# 'chip': 'CHIP', 'snack': 'SNACK'}
