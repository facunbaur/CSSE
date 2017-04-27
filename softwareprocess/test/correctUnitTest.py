import unittest
import softwareprocess.operations.correct as correct

class correctUnitTest(unittest.TestCase):

    def test_010_010_shouldExtractLatitude(self):
        test_input = {'body': 'betelgeuse'}
        expected = {'sha': '270d59.1', 'declination': '7d24.3'}
        actual = correct.extractMeasurement(test_input, 'lat', -90, 90)
        self.assertEqual(actual, expected, 'Should extract latitude')
    pass
