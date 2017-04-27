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



    # LONGITUDE TESTS

    def test_010_010_shouldExtractLongitude(self):
        test_input = {'long': '45d0.0'}
        expected = 45
        actual = correct.extractMeasurement(test_input, 'long', 0, 360)
        self.assertAlmostEqual(actual, expected, 3, 'Should extract longitude')

    def test_010_090_handleMissingLongitude(self):
        test_input = {}
        expected = {'error': 'missing mandatory field long'}
        try:
            actual = correct.extractMeasurement(test_input, 'long', 0, 360)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleLowLongitude(self):
        test_input = {'long': '-0d1.0'}
        expected = {'long': '-0d1.0', 'error': 'long is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'long', 0, 360)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleHighLongitude(self):
        test_input = {'long': '360d1.0'}
        expected = {'long': '360d1.0', 'error': 'long is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'long', 0, 360)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')


    # Altitude TESTS

    def test_010_010_shouldExtractAltitude(self):
        test_input = {'altitude': '45d0.0'}
        expected = 45
        actual = correct.extractMeasurement(test_input, 'altitude', 0, 90)
        self.assertAlmostEqual(actual, expected, 3, 'Should extract altitude')

    def test_010_090_handleMissingAltitude(self):
        test_input = {}
        expected = {'error': 'missing mandatory field altitude'}
        try:
            actual = correct.extractMeasurement(test_input, 'altitude', 0, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleLowAltitude(self):
        test_input = {'altitude': '-0d1.0'}
        expected = {'altitude': '-0d1.0', 'error': 'altitude is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'altitude', 0, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleHighAltitude(self):
        test_input = {'altitude': '90d1.0'}
        expected = {'altitude': '90d1.0', 'error': 'altitude is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'altitude', 0, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    # ASSUMED LATITUDE

    def test_010_010_shouldExtractAssumedLatitude(self):
        test_input = {'assumedLat': '45d0.0'}
        expected = 45
        actual = correct.extractMeasurement(test_input, 'assumedLat', -90, 90)
        self.assertAlmostEqual(actual, expected, 3, 'Should extract assumed latitude')

    def test_010_090_handleMissingAssumedLatitude(self):
        test_input = {}
        expected = {'error': 'missing mandatory field assumedLat'}
        try:
            actual = correct.extractMeasurement(test_input, 'assumedLat', -90, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleLowAssumedLatitude(self):
        test_input = {'assumedLat': '-90d1.0'}
        expected = {'assumedLat': '-90d1.0', 'error': 'assumedLat is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'assumedLat', -90, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleHighAssumedLatitude(self):
        test_input = {'assumedLat': '90d1.0'}
        expected = {'assumedLat': '90d1.0', 'error': 'assumedLat is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'assumedLat', -90, 90)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')