#!/usr/local/bin/python3

import sys


string = str(sys.argv[1])
result = ''

sub = {
    '0': chr(8320),
    '1': chr(8321),
    '2': chr(8322),
    '3': chr(8323),
    '4': chr(8324),
    '5': chr(8325),
    '6': chr(8326),
    '7': chr(8327),
    '8': chr(8328),
    '9': chr(8329),
}

for c in string:
    try:
        result += sub[c]
    except KeyError:
        pass

print(result)

