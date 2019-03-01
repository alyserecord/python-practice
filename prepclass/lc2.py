stop_words_list = ['a', 'an', 'and', 'in', 'is',
                   'of', 'or', 'that', 'the', 'to']


text = """Data science is an interdisciplinary field of scientific
methods, processes, algorithms and systems to extract knowledge or
insights from data in various forms, either structured or unstructured,
similar to data mining."""
text_list = text.lower().split()

# no_stops_list = []
# for word in text_list:
#     if word not in stop_words_list:
#         no_stops_list.append(word)


no_stops_list = [x for x in text_list if x not in stop_words_list]

print(no_stops_list)