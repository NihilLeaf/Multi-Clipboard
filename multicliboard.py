import sys
import clipboard
import json

#Fuction to add items to a json file
def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

#Fuction to read the keys and values of the json file
def load_json(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data


#Check if the value we pass after the py file on cmd or terminal is only 1
if len(sys.argv) == 2:
    command = sys.argv[1]
    #Check if the values are the choosen.
    if command == 'save':
        print('save')
    elif command == 'load':
        print('load')
    elif command == 'list':
        print('list')
    else:
        print('Unknown value')
else:
    print('Type a value!')

