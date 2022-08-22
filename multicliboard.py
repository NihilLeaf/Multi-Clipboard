import sys
from time import sleep, time
import clipboard
import json

SAVED_DATA = 'clipboard.json'

#Fuction to add items to a json file
def save_data(filepath, data):
    with open(filepath, 'w+') as f:
        json.dump(data, f)

#Fuction to read the keys and values of the json file
def load_data(filepath):
    try:
        with open(filepath, 'r+') as f:
            data = json.load(f)
            return data
    except:
        return {}

#Check if the value we pass after the py file on cmd or terminal is only 1
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    #Check if the values are the choosen.
    if command == 'add':
        key = input('Enter a key: ').lower()
        data[key] = clipboard.paste()
        save_data(SAVED_DATA ,data)
        print('Data saved!')

    elif command == 'load':
        key = input('Enter a key: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard!')
        else:
            print('Key not founded')
            print("...")
            sleep(1)
            while True:
                key = input('Enter a key again: ')
                if key in data:
                    clipboard.copy(data[key])
                    print('Data copied to clipboard!')
                    break
                else:
                    print('Key not founded')
                    print('...')
                    sleep(1)

    elif command == 'list':
        print(data)

    elif command == 'del':
        key = str(input('What key to delete? '))
        if key in data:
            data.pop(key)
            with open(SAVED_DATA, 'w') as f:
                json.dump(data, f)
        
        else:
            print('Key not indentified!')

    else:
        print('Unknown value')

else:
    print('Type a value!')

