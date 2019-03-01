words = input('Enter words to transform to lowercase here. Separate them with spaces:')

# words = 'RADIO aStRoNoMy Pulsar'

result = tuple((word, word.lower()) for word in words.split())


print(result)

# (('RADIO', 'radio'), ('aStRoNoMy', 'astronomy'), 
# ('Pulsar', 'pulsar'))