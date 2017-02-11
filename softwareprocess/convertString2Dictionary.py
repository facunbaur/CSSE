from __future__ import print_function
import urllib


def convertString2Dictionary(inputString = ""):
    print(urllib.unquote(inputString))
    errorDict = {'error':'true'}
    return errorDict


def is_valid_key(input_string = ""):
    return len(input_string) > 0 and input_string.isalnum() and input_string[:1].isalpha()


def is_valid_value(input_string = ""):
    return input_string.isalnum()

