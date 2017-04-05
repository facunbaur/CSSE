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

    def test_010_020_shouldExtractBodyUppercase(self):
        test_input = {'body': 'BETELGEUSE'}
        expected = {'sha': '270d59.1', 'declination': '7d24.3'}
        actual = predict.extractBody(test_input)
        self.assertEqual(actual, expected, 'Should extract uppercase body')

    def test_010_030_shouldExtractBodyMixedcase(self):
        test_input = {'body': 'BeTeLGeUsE'}
        expected = {'sha': '270d59.1', 'declination': '7d24.3'}
        actual = predict.extractBody(test_input)
        self.assertEqual(actual, expected, 'Should extract mixedcase body')

    # SadPath
    def test_010_710_shouldHandleMissingBody(self):
        test_input = {}
        expected = {'error': 'mandatory information is missing'}
        actual = predict.extractBody(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle missing body')
