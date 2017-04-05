import unittest

import softwareprocess.operations.predict as predict

class predictUnitTest(unittest.TestCase):

    # 010 extractBody
    # Desired level of confidence: Boundary-Value analysis
    #
    # HappyPath
    #   correct body, all lowercase.
    #   correct body, all uppercase.
    #   correct body, mixed case.
    # SadPath
    #   missing body
    #   body is not a string
    #   body is not a valid star name
    def test_010_010_shouldExtractBodyLowercase(self):
        test_input = {'body': 'betelgeuse'}
        expected = {'sha': '270d59.1', 'declination': '7d24.3'}
        actual = predict.extractBody(test_input)
        self.assertEqual(actual, expected, 'Should extract lowercase body')

