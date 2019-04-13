test orange what is this
def counter(words,letters):
  '''
  Write a function that counts the number of times a
  letter appears in a document. The output should be a dict.
  '''
  l = {}
  
  for i in list(letters):
    count_of_letter = 0
    for item in words:
      if item == i:
        count_of_letter += 1
    l.update({i:count_of_letter})

  return l
