import unittest
import softwareprocess.operations.correct as correct

class correctUnitTest(unittest.TestCase):

    def test_010_010_shouldExtractLatitude(self):
        test_input = {'lat': '45d0.0'}
        expected = 45
        actual = correct.extractMeasurement(test_input, 'lat', -90, 90)
        self.assertAlmostEqual(actual, expected, 3, 'Should extract latitude')
