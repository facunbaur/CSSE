from __future__ import print_function
import urllib


def convertString2Dictionary(inputString = ""):
    error_dict = {'error':'true'}
    out_dict = {}
    print(urllib.unquote(inputString))
    key_value_pairs_list = [str.strip() for str in urllib.unquote(inputString).split(',')]
    if len(key_value_pairs_list) == 0:
        return error_dict

    for key_value_pair in key_value_pairs_list:
        # Split each instance of "key = value" into a list based on spaces.
        key_value_list = [str.strip() for str in key_value_pair.split('=')]

        # In order to be valid, this must be a list of the form [key, value]
        if len(key_value_list) != 2:
            return error_dict

        # Validate the key.
        key = key_value_list[0]
        if not is_valid_key(key):
            return error_dict

        # Validate the value.
        value = key_value_list[1]
        if not is_valid_value(value):
            return error_dict

        # No duplicate keys are allowed.
        if key in out_dict:
            return error_dict

        # The key / value pair seems valid! We can add it to our dictionary.
        out_dict[key] = value

    return out_dict


def is_valid_key(input_string = ""):
    return len(input_string) > 0 and input_string.isalnum() and input_string[:1].isalpha()


def is_valid_value(input_string = ""):
    return input_string.isalnum()

