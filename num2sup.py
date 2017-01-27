#!/usr/local/bin/python3

import sys


string = str(sys.argv[1])
result = ''

sup = {
    '0': chr(8304),
    '1': chr(185),
    '2': chr(178),
    '3': chr(179),
    '4': chr(8308),
    '5': chr(8309),
    '6': chr(8310),
    '7': chr(8311),
    '8': chr(8312),
    '9': chr(8313),
}

for c in string:
    try:
        result += sup[c]
    except KeyError:
        pass

print(result)

