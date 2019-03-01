state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau',
                    'California': 'Sacramento', 'Georgia': 'Atlanta',
                    'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                    'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

user_state = input('Enter the name of a state: ').lower()
found_state = False

for state, city in state_dictionary.items():
    if user_state == state.lower():
        print (city)
        found_state = True
        break
if found_state == False:
    print('Capital unknown')