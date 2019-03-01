my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago',
          'New York': 'Albany', 'Iowa': 'Des Moines',
          'California': 'Sacramento', 'Utah': 'Salt Lake City',
          'Ohio': 'Columbus'}
for state, city in my_dct.items():
    if city[0] == 'S':
        print(city)