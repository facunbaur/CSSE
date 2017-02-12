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

    error_dict = {'error':'true'} # Returned in the event of an error.
    out_dict = {}                 # Holds successful key-value pairs.

    # Separate the input string on commas and strip whitespace between elements.
    key_value_pairs_list = [str.strip() for str in urllib.unquote(inputString).split(',')]

    # We must have at least one key-value pair.
    if len(key_value_pairs_list) == 0:
        return error_dict

    for key_value_pair in key_value_pairs_list:
        # Split each instance of "key = value" into a list based on spaces.
        key_value_list = [str.strip() for str in key_value_pair.split('=')]

        # In order to be valid, this must be a list of the form [key, value].
        # It must therefore have a length of 2.
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
    """
    Returns true if and only if the given string is of nonzero length, and contains only alphanumeric characters,
    starting with a letter.
    :param input_string: The string to test for validity.
    :return: True iff input_string is a valid key.
    """
    return len(input_string) > 0 and input_string.isalnum() and input_string[:1].isalpha()


def is_valid_value(input_string = ""):
    """
    Returns true if and only if the given string is of nonzero length, and contains only alphanumeric characters.
    :param input_string: The string to test for validity.
    :return: True iff input_string is a valid value.
    """
    return input_string.isalnum()

