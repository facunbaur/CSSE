import unittest
import softwareprocess.operations.adjust as adjust
import softwareprocess.operations.correct as correct
import softwareprocess.operations.locate as locate
import softwareprocess.operations.predict as predict



class operationsTest(unittest.TestCase):

    # 100 correct
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     sighting: dictionary containing 'op': 'correct', validated.
    #       outputs:    sighting passed, unchanged.
    #   Happy Path
    #       dictionary containing only op
    #       dictionary containing extra values
    #
    # Happy Path
    def test100_010_ShouldPassPlainDictionary(self):
        sighting = dict()
        sighting['op'] = 'correct'
        actual = correct.correct(sighting)
        self.assertEqual(actual, sighting, 'Should return unmodified')

    def test100_020_ShouldPassDictionaryWithAddedEntry(self):
        sighting = dict()
        sighting['op'] = 'correct'
        sighting['extra'] = 'ignore me'
        actual = correct.correct(sighting)
        self.assertEqual(actual, sighting, 'Should return unmodified')

    # 200 locate
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     sighting: dictionary containing 'op': 'locate', validated.
    #       outputs:    sighting passed, unchanged.
    #   Happy Path
    #       dictionary containing only op
    #       dictionary containing extra values
    #
    # Happy Path
    def test200_010_ShouldPassPlainDictionary(self):
        sighting = dict()
        sighting['op'] = 'locate'
        actual = locate.locate(sighting)
        self.assertEqual(actual, sighting, 'Should return unmodified')

    def test200_020_ShouldPassDictionaryWithAddedEntry(self):
        sighting = dict()
        sighting['op'] = 'locate'
        sighting['extra'] = 'ignore me'
        actual = locate.locate(sighting)
        self.assertEqual(actual, sighting, 'Should return unmodified')

    # 300 predict
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     sighting: dictionary containing 'op': 'predict', validated.
    #       outputs:    sighting passed, unchanged.
    #   Happy Path
    #       dictionary containing only op
    #       dictionary containing extra values
    #
    # Happy Path
    def test300_010_ShouldPassPlainDictionary(self):
        sighting = dict()
        sighting['op'] = 'predict'
        actual = predict.predict(sighting)
        self.assertEqual(actual, sighting, 'Should return unmodified')

    def test300_020_ShouldPassDictionaryWithAddedEntry(self):
        sighting = dict()
        sighting['op'] = 'predict'
        sighting['extra'] = 'ignore me'
        actual = predict.predict(sighting)
        self.assertEqual(actual, sighting, 'Should return unmodified')

    # 510 degreeStringToDegrees
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     degreeString: unvalidated string of the form '<x>d<y>',
    #                   where x is the amount of degrees, and y is the amount of minutes.
    #                   This value must be >= '0d0.1' and < '90d0.0'
    #
    #       outputs:    sighting passed, unchanged.
    #   Happy Path
    #       nominal x, nominal y    '45d30.0'   -> 45.5
    #       nominal x, low y        '45d0.0'    -> 45.0
    #       nominal x, integer y    '45d0'      -> 45.0
    #       nominal x, high y       '45d59.9'   -> 45.99833..
    #       low x, nominal y        '0d30.0'    -> 0.5
    #       low x, low y            '0d0.1'     -> 0.00166...
    #       low x, high y           '0d59.9'    -> 0.99833...
    #       high x, nominal y       '89d30.0'   -> 89.5
    #       high x, low y           '89d0.0'    -> 89.0
    #       high x, high y          '89d59.9'   -> 89.99833...
    #   Sad Path
    #       no 'd'                  '85'        -> raise ValueError
    #       multiple 'd's           '45dd30.0'  -> raise ValueError
    #       illegal characters      '45d&30.0'  -> raise ValueError
    #       negative x              '-15d30.0'  -> raise ValueError
    #       negative y              '45d-15.0'  -> raise ValueError
    #       too large y             '45d60.0'   -> raise ValueError
    #       value too small         '0d0.0'     -> raise ValueError
    #       value too large         '90d0.0'    -> raise ValueError
    #       non-integer x           '45.0d30.0' -> raise ValueError
    # Happy Path
    def test510_010ShouldCalculateNominalXNominalY(self):
        actual = adjust.degreeStringToDegrees('45d30.0')
        self.assertAlmostEquals(actual, 45.5, 5)

    def test510_020ShouldCalculateNominalXLowY(self):
        actual = adjust.degreeStringToDegrees('45d0.0')
        self.assertAlmostEquals(actual, 45.0, 5)

    def test510_030ShouldCalculateNominalXIntegerY(self):
        actual = adjust.degreeStringToDegrees('45d0')
        self.assertAlmostEquals(actual, 45.0, 5)

    def test510_040ShouldCalculateNominalXHighY(self):
        actual = adjust.degreeStringToDegrees('45d59.9')
        self.assertAlmostEquals(actual, 45.99833333, 5)

    def test510_050ShouldCalculateLowXLowY(self):
        actual = adjust.degreeStringToDegrees('0d0.1')
        self.assertAlmostEquals(actual, 0.001666667, 5)

    def test510_060ShouldCalculateLowXNominalY(self):
        actual = adjust.degreeStringToDegrees('0d30.0')
        self.assertAlmostEquals(actual, 0.5, 5)

    def test510_070ShouldCalculateLowXHighY(self):
        actual = adjust.degreeStringToDegrees('0d59.9')
        self.assertAlmostEquals(actual, 0.99833333, 5)

    def test510_080ShouldCalculateHighXLowY(self):
        actual = adjust.degreeStringToDegrees('89d0.0')
        self.assertAlmostEquals(actual, 89.0, 5)

    def test510_090ShouldCalculateHighXNominalY(self):
        actual = adjust.degreeStringToDegrees('89d30.0')
        self.assertAlmostEquals(actual, 89.5, 5)

    def test510_100ShouldCalculateHighXHighY(self):
        actual = adjust.degreeStringToDegrees('89d59.9')
        self.assertAlmostEquals(actual, 89.99833333, 5)
    # Sad Path

