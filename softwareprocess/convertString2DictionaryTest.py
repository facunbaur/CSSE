from __future__ import print_function
import unittest

from convertString2Dictionary import convertString2Dictionary, is_valid_key, is_valid_value


given_NonErrorTests = [
    {
        'input': 'abc%3D123',
        'expected': {'abc': '123'},
    }, {
        'input':  'function%20%3D%20getstars',
        'expected': {'function': 'getstars'},
    }, {
        'input': 'function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse',
        'expected': {'function': 'calculatePosition', 'sighting': 'Betelgeuse'},
    }
]

given_ErrorTests = [
    {
        'input':  'function%20%3D%20get_stars',     # Underscores are not allowed.
        'expected': {'error': 'true'},
    }, {
        'input':  'key%3Dvalue%2C%20key%3Dvalue',   # Duplicate key.
        'expected': {'error': 'true'},
    }, {
        'input': 'key%3D',                          # Missing value.
        'expected': {'error': 'true'},
    }, {
        'input': 'value',                           # Missing key.
        'expected': {'error': 'true'},
    }, {
        'input': '1key%3Dvalue',                    # Key is invalid.
        'expected': {'error': 'true'},
    }, {
        'input':  'k%20e%20y%20%3D%20value',        # Key has embedded blank characters.
        'expected': {'error': 'true'},
    }, {
        'input':  '',                               # No key - value pairs are present.
        'expected': {'error': 'true'},
    }, {
        'input': 'key1%3Dvalue%3B%20key2%3Dvalue',  # Key - value pairs are not separated by a legal separator.
        'expected': {'error': 'true'},
    }
]

key_validation_tests = [
    {
        'input': 'aBc',
        'expected': True,
    }, {
        'input': 'Abc',
        'expected': True,
    }, {
        'input': 'abc123',
        'expected': True,
    }, {
        'input': 'a b c',       # Spaces are not allowed.
        'expected': False,
    }, {
        'input': ' abc',        # Spaces are not allowed.
        'expected': False,
    }, {
        'input': '1abc',        # Keys cannot start with a number.
        'expected': False,
    }, {
        'input': 'a_b_c',       # Underscores are not allowed.
        'expected': False,
    }, {
        'input': '',            # Must be nonzero length.
        'expected': False,
    }
]

value_validation_tests = [
    {
        'input': 'aBc',
        'expected': True,
    }, {
        'input': 'Abc',
        'expected': True,
    }, {
        'input': 'abc123',
        'expected': True,
    }, {
        'input': 'a b c',       # Spaces are not allowed.
        'expected': False,
    }, {
        'input': ' abc',        # Spaces are not allowed.
        'expected': False,
    }, {
        'input': '1abc',        # Unlike keys, values cannot start with a number.
        'expected': True,
    }, {
        'input': 'a_b_c',       # Underscores are not allowed.
        'expected': False,
    }, {
        'input': '',            # Must be nonzero length.
        'expected': False,
    }
]

class TestConvertString2Dictionary(unittest.TestCase):

    def run_test(self, function, testdata=[]):
        for test in testdata:
            print('Testing input "{0}"'.format(test['input']))
            returned = function(test['input'])
            self.assertEqual(returned, test['expected'])

    def test_given_nonerror(self):
        self.run_test(convertString2Dictionary, given_NonErrorTests)

    def test_given_error(self):
        self.run_test(convertString2Dictionary, given_ErrorTests)

    def test_key_validation(self):
        self.run_test(is_valid_key, key_validation_tests)

    def test_value_validation(self):
        self.run_test(is_valid_value, value_validation_tests)

if __name__ == '__main__':
    unittest.main()
