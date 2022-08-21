import sys
import clipboard
import json

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
        print('Unknow value')


