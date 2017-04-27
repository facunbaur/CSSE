import unittest
import softwareprocess.operations.correct as correct

class correctUnitTest(unittest.TestCase):

    def test_010_010_shouldExtractLatitude(self):
        test_input = {'lat': '45d0.0'}
        expected = 45
        actual = correct.extractMeasurement(test_input, 'lat', -90, 90)
        self.assertAlmostEqual(actual, expected, 3, 'Should extract latitude')

    def test_010_090_handleMissingLatitude(self):
        test_input = {}
        expected = {'error': 'missing mandatory field lat'}
        try:
            actual = correct.extractMeasurement(test_input, 'lat', -90, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleLowLatitude(self):
        test_input = {'lat': '-90d1.0'}
        expected = {'lat': '-90d1.0', 'error': 'lat is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'lat', -90, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleHighLatitude(self):
        test_input = {'lat': '90d1.0'}
        expected = {'lat': '90d1.0', 'error': 'lat is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'lat', -90, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')
