from __future__ import print_function
import unittest

from convertString2Dictionary import convertString2Dictionary


givenTests = [
    {
        'input': 'abc%3D123',
        'expected': {'abc': '123'},
    }, {
        'input':  'function%20%3D%20get stars',
        'expected': {'function': 'get stars'},
    }, {
        'input': 'function%3D%20calculatePosition%2C%20sighting%3DBetelgeuse',
        'expected': {'function': 'calculatePosition', 'sighting': 'Betelgeuse'},
    }, {
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


class TestConvertString2Dictionary(unittest.TestCase):

    def test_given(self):
        for test in givenTests:
            returned = convertString2Dictionary(test['input'])
            print('Testing input ', test['input'])
            self.assertEqual(returned, test['expected'])

if __name__ == '__main__':
    unittest.main()
