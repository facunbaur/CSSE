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
    #   date has < 3 fields
    #   date has > 3 fields
    #   date ranges are not strings of integers
    #   a date range is too large.
    #   year is before 2001
    def test_020_010_ShouldExtractValidDate(self):
        test_input = {'date': '2011-3-15'}
        expected = datetime.date(2011, 3, 15)
        actual = predict.extractDate(test_input)
        self.assertEqual(actual, expected, 'Should extract nominal date')

    def test_020_020_ShouldExtractDefaultDate(self):
        test_input = {}
        expected = datetime.date(2001, 01, 01)
        actual = predict.extractDate(test_input)
        self.assertEqual(actual, expected, 'Should extract default date')

    # SadPaths
    def test_020_710_ShouldHandleNonStringDate(self):
        test_input = {'date': 17}
        expected = {'date': 17, 'error': 'invalid date'}
        actual = predict.extractDate(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle non string date')

    def test_020_720_ShouldHandleTooFewFields(self):
        test_input = {'date': '2011-10'}
        expected = {'date': '2011-10', 'error': 'invalid date'}
        actual = predict.extractDate(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle too few fields')

    def test_020_730_ShouldHandleTooManyFields(self):
        test_input = {'date': '2011-10-10-10'}
        expected = {'date': '2011-10-10-10', 'error': 'invalid date'}
        actual = predict.extractDate(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle too many fields')

    def test_020_740_ShouldHandleNonIntegerFields(self):
        test_input = {'date': '2011-a-b'}
        expected = {'date': '2011-a-b', 'error': 'invalid date'}
        actual = predict.extractDate(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle non integer fields')

    def test_020_750_ShouldHandleInvalidFields(self):
        test_input = {'date': '2011-13-01'}
        expected = {'date': '2011-13-01', 'error': 'invalid date'}
        actual = predict.extractDate(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle invalid fields')

    def test_020_760_ShouldHandleYearBefore2001(self):
        test_input = {'date': '2000-10-10'}
        expected = {'date': '2000-10-10', 'error': 'invalid date'}
        actual = predict.extractDate(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle year before 2001')

    # 030 extractTime
    #
    # HappyPath
    #   Valid time.
    #   Missing time, return default value.
    # SadPath
    #   time is not a string
    #   time has < 3 fields
    #   time has > 3 fields
    #   time ranges are not strings of integers
    #   a time range is too large.
    # HappyPath
    def test_030_010_ShouldExtractNominalTime(self):
        test_input = {'time': '12:15:57'}
        expected = datetime.time(12, 15, 57)
        actual = predict.extractTime(test_input)
        self.assertEqual(actual, expected, 'Should extract nominal time')

    def test_030_020_ShouldExtractDefaultTime(self):
        test_input = {}
        expected = datetime.time(0, 0, 0)
        actual = predict.extractTime(test_input)
        self.assertEqual(actual, expected, 'Should extract default time')

    # SadPath
    def test_030_710_ShouldHandleNonStringTime(self):
        test_input = {'time': 17}
        expected = {'time': 17, 'error': 'invalid time'}
        actual = predict.extractTime(test_input)
        self.assertIsNone(actual)
        self.assertEqual(test_input, expected, 'Should handle a non-string time')
