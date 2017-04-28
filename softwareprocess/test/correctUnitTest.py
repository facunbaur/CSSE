import unittest
import softwareprocess.operations.correct as correct
import softwareprocess.operations.util as util

class correctUnitTest(unittest.TestCase):

    def test_000_010_shouldCorrect(self):
        test_input = {
            'lat': '16d32.3',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': '16d32.3',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'correctedDistance': '3950',
            'correctedAzimuth': '164d42.9'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

    def test_000_050_shouldHandleLowLat(self):
        test_input = {
            'lat': '-90d0.0',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': '-90d0.0',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'error': 'lat is invalid'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

    def test_000_051_shouldHandleHighLat(self):
        test_input = {
            'lat': '90d0.0',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': '90d0.0',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'error': 'lat is invalid'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

    def test_000_052_shouldHandleNumLat(self):
        test_input = {
            'lat': 1,
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': 1,
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'error': 'lat is invalid'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

    def test_000_053_shouldHandleLowLon(self):
        test_input = {
            'lat': '16d32.3',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': '16d32.3',
            'long': '95d41.6',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'correctedAzimuth': '164d42.9',
            'correctedDistance': '3950'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

    def test_000_054_shouldHandleHighLon(self):
        test_input = {
            'lat': '16d32.3',
            'long': '360d0.0',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': '16d32.3',
            'long': '360d0.0',
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'error': 'long is invalid'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

    def test_000_055_shouldHandleNumLon(self):
        test_input = {
            'lat': '16d32.3',
            'long': 1,
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3'
        }
        expected = {
            'lat': '16d32.3',
            'long': 1,
            'altitude': '13d42.3',
            'assumedLat': '-53d38.4',
            'assumedLong': '74d35.3',
            'error': 'long is invalid'
        }
        actual = correct.correct(test_input)
        self.assertEqual(expected, actual)

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

    # Assumed LONGITUDE TESTS

    def test_010_010_shouldExtractAssumedLongitude(self):
        test_input = {'assumedLong': '45d0.0'}
        expected = 45
        actual = correct.extractMeasurement(test_input, 'assumedLong', 0, 360)
        self.assertAlmostEqual(actual, expected, 3, 'Should extract assumed longitude')

    def test_010_090_handleMissingAssumedLongitude(self):
        test_input = {}
        expected = {'error': 'missing mandatory field assumedLong'}
        try:
            actual = correct.extractMeasurement(test_input, 'assumedLong', 0, 360)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleLowAssumedLongitude(self):
        test_input = {'assumedLong': '-0d1.0'}
        expected = {'assumedLong': '-0d1.0', 'error': 'assumedLong is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'assumedLong', 0, 360)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_010_091_handleHighAssumedLongitude(self):
        test_input = {'assumedLong': '360d1.0'}
        expected = {'assumedLong': '360d1.0', 'error': 'assumedLong is invalid'}
        try:
            actual = correct.extractMeasurement(test_input, 'assumedLong', 0, 360)
        except ValueError:
            self.assertEqual(test_input, expected, 'Should have error')
            return
        self.assertTrue(False, 'Did not raise error')

    def test_020_010_shouldCalculateIntermediateDistance(self):
        expected = -0.789410565
        inLat = util.degreeStringToDegrees('16d32.3', False)
        inLon = util.degreeStringToDegrees('95d41.6', False)
        inAssumedLat = util.degreeStringToDegrees('-53d38.4', False)
        inAssumedLon = util.degreeStringToDegrees('74d35.3', False)
        actual = correct.calculateIntermediateDistance(inLat, inAssumedLat, inLon, inAssumedLon)
        self.assertAlmostEqual(expected, actual, 3)

    def test_030_010_shouldCalculateCorrectedDistance(self):
        expected = 3950
        inLat = util.degreeStringToDegrees('16d32.3', False)
        inLon = util.degreeStringToDegrees('95d41.6', False)
        altitude = util.degreeStringToDegrees('13d42.3', False)
        inAssumedLat = util.degreeStringToDegrees('-53d38.4', False)
        inAssumedLon = util.degreeStringToDegrees('74d35.3', False)
        actual = correct.calculateCorrectedDistance(inLat, inAssumedLat, altitude, inLon, inAssumedLon)
        self.assertAlmostEqual(expected, actual, 6)

    def test_040_010_shouldCalculateCorrectedAzimuth(self):
        expected = '164d42.9'
        inLat = util.degreeStringToDegrees('16d32.3', False)
        inLon = util.degreeStringToDegrees('95d41.6', False)
        altitude = util.degreeStringToDegrees('13d42.3', False)
        inAssumedLat = util.degreeStringToDegrees('-53d38.4', False)
        inAssumedLon = util.degreeStringToDegrees('74d35.3', False)
        actual = correct.calculateCorrectedAzimuth(inLat, inAssumedLat, inLon, inAssumedLon)
        self.assertEqual(expected, actual)
