"""
    convertString2Dictionary.py contains convertString2Dictionary,
    which will convert a valid percent-encoded input string to a
    dictionary, along with various helper functions.

    Created on 2/11/2017
    Last Modified on 2/13/2017

    @author: Mitchell Price
"""
from __future__ import print_function
import urllib


def convertString2Dictionary(inputString = ""):
    """
    convertString2Dictionary will take an input string, which consists of a percent-encoded string holding
    comma separated key-value pairs of the form <key>=<value>, produce a dictionary storing the given key-value pairs.
    Both keys and values must be alphanumeric strings. Additionally, keys must begin with a letter and be unique.
    :param inputString: A string to be converted to a dictionary.
    :return: A dictionary represented by the input string. In the event of an error, {'error' : 'true'} will be returned
    """

    errorDict = {'error': 'true'} # Returned in the event of an error.
    outDict = {}                 # Holds successful key-value pairs.

    # Separate the input string on commas and strip whitespace between elements.
    keyValuePairsList = [str.strip() for str in urllib.unquote(inputString).split(',')]

    # We must have at least one key-value pair.
    if len(keyValuePairsList) == 0:
        return errorDict

    for keyValuePair in keyValuePairsList:
        # Split each instance of "key = value" into a list based on spaces.
        keyValueList = [str.strip() for str in keyValuePair.split('=')]

        # In order to be valid, this must be a list of the form [key, value].
        # It must therefore have a length of 2.
        if len(keyValueList) != 2:
            return errorDict

        # Validate the key.
        key = keyValueList[0]
        if not isValidKey(key):
            return errorDict

        # Validate the value.
        value = keyValueList[1]
        if not isValidValue(value):
            return errorDict

        # No duplicate keys are allowed.
        if key in outDict:
            return errorDict

        # The key / value pair seems valid! We can add it to our dictionary.
        outDict[key] = value

    return outDict


def isValidKey(inputString =""):
    """
    Returns true if and only if the given string is of nonzero length, and contains only alphanumeric characters,
    starting with a letter.
    :param inputString: The string to test for validity.
    :return: True iff input_string is a valid key.
    """
    return len(inputString) > 0 and inputString.isalnum() and inputString[:1].isalpha()


def isValidValue(inputString =""):
    """
    Returns true if and only if the given string is of nonzero length, and contains only alphanumeric characters.
    :param inputString: The string to test for validity.
    :return: True iff input_string is a valid value.
    """
    return inputString.isalnum()

