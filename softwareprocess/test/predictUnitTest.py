import unittest
import datetime

import softwareprocess.operations.predict as predict

class predictUnitTest(unittest.TestCase):

    # 010 extractBody
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

    def test_010_720_shouldHandleNonStringBody(self):
        test_input = {'body': 7}
        expected = {'body': 7, 'error': 'invalid body'}
        actual = predict.extractBody(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle non-string body')

    def test_010_730_shouldHandleNonExistentBody(self):
        test_input = {'body': 'unknown'}
        expected = {'body': 'unknown', 'error': 'star not in catalog'}
        actual = predict.extractBody(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle nonexistent star name')

    # 020 extractDate
    #
    # HappyPath
    #   Valid date.
    #   Missing date, return default value.
    # SadPath
    #   date is not a string
    #   date is not 3 '-' separated fields
    #   a date range is too large.
    #   year is before 2001
    def test_020_010_ShouldExtractValidDate(self):
        test_input = {'date': '2011-3-15'}
        expected = datetime.date(2011, 3, 15)
        actual = predict.extractDate(test_input)
        self.assertEqual(actual, expected, 'Should extract nominal date')
