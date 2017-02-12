from __future__ import print_function
import unittest

from convertString2Dictionary import convertString2Dictionary, is_valid_key, is_valid_value

# All of the provided tests that are expected to complete successfully.
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

# All of the provided tests that are expected to fail.
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

# Tests for is_valid_key.
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

# Tests for is_valid_value.
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
    """
    TestConvertString2Dictionary contains tests for ConvertString2Dictionary and all helper methods.
    """

    def run_test(self, function, test_data=[]):
        """
        Will run a test of tests against a given function.
        :param function: The function to test.
        :param test_data: A list of tests to run. They should be of the form
        { 'input' <sample input> : 'expected' < expected output> }
        """
        for test in test_data:
            self.assertEqual(function(test['input']), test['expected'])

    def test_given_non_error(self):
        """
        Test convertString2Dictionary against all provided tests that are expected to complete successfully.
        """
        self.run_test(convertString2Dictionary, given_NonErrorTests)

    def test_given_error(self):
        """
        Test convertString2Dictionary against all provided tests that are expected to complete unsuccessfully.
        """
        self.run_test(convertString2Dictionary, given_ErrorTests)

    def test_key_validation(self):
        """
        Test is_valid_key.
        """
        self.run_test(is_valid_key, key_validation_tests)

    def test_value_validation(self):
        """
        Test is_valid_value.
        """
        self.run_test(is_valid_value, value_validation_tests)

if __name__ == '__main__':
    unittest.main()
