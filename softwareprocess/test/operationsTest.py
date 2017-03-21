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
    #       outputs:    The value, in degrees.
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
    def test510_700FailIfNoD(self):
        expectedString = "No 'd' delimiter"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('85')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_710FailTooManyDs(self):
        expectedString = "Too many 'd' delimiters"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('45dd30.0')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_720NegativeX(self):
        expectedString = "Negative number of degrees"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('-15d30.0')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_730NegativeY(self):
        expectedString = "Negative number of minutes"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('45d-15.0')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_740TooLargeY(self):
        expectedString = "Number of minutes too large"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('45d60.0')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_750TooSmallValue(self):
        expectedString = "Measurement too small"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('0d0.0')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_760TooLargeValue(self):
        expectedString = "Measurement too large"
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('90d0.0')
        self.assertEquals(expectedString, context.exception.args[0][0:len(expectedString)])

    def test510_770TooLargeValue(self):
        with self.assertRaises(ValueError) as context:
            adjust.degreeStringToDegrees('45.0d0.0')

    # 520 degreesToDegreesString
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     degreeString: validated degree.
    #       outputs:    a string indicating the degree/minutes of the value.
    #   Happy Path
    #       Nominal x, Nominal y    45.5    -> '45d30.0'
    #       Nominal x, Zero y       45.0    -> '45d0.0'
    #       Low x, Nominal y        0.5     -> '0d30.0'
    #       High x, High y       89.99833333     -> '89d59.9'
    #   Sad Path
    #       None
    # Happy Path
    def test520_010NominalXNominalY(self):
        actual = adjust.degreesToDegreeString(45.5)
        self.assertEqual(actual, '45d30.0')

    def test520_020NominalXZeroY(self):
        actual = adjust.degreesToDegreeString(45.0)
        self.assertEqual(actual, '45d0.0')

    def test520_030LowXNominalY(self):
        actual = adjust.degreesToDegreeString(0.5)
        self.assertEqual(actual, '0d30.0')

    def test520_040HighXHighY(self):
        actual = adjust.degreesToDegreeString(89.9983333333)
        self.assertEqual(actual, '89d59.9')

    # 410 extractHeight
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     sighting, a dictionary containing 'height', which should be a string
    #                   representation of a non-negative numeric value.
    #       outputs:    the non-negative numeric value represented.
    #                   otherwise, sets the error field of the dictionary and raises value error.
    #   Happy Path
    #       No Value                NONE    -> 0
    #       Low Value               '0'     -> 0
    #       Nominal Value         '25.2'    -> 25.2
    #       High Value            '999999.9'-> 999999.9
    #   Sad Path
    #       Non - String Value     'height' : 20    -> 'error': 'height is invalid', ValueError()
    #       String, non numeric    'height' : 'abc' -> 'error': 'height is invalid', ValueError()
    #       negative value         'height': '-1.0' -> 'error': 'height is invalid', ValueError()
    # Happy Path
    def test410_010_ShouldGetDefaultValue(self):
        actual = adjust.extractHeight({})
        self.assertAlmostEquals(actual, 0.0, 5)

    def test410_020_ShouldHandleLowValue(self):
        actual = adjust.extractHeight({'height': '0'})
        self.assertAlmostEquals(actual, 0.0, 5)

    def test410_030_ShouldHandleNominalValue(self):
        actual = adjust.extractHeight({'height': '25.2'})
        self.assertAlmostEquals(actual, 25.2, 5)

    def test410_040_ShouldHandleHighValue(self):
        actual = adjust.extractHeight({'height': '999999.9'})
        self.assertAlmostEquals(actual, 999999.9, 5)

    # Sad Paths
    def test410_910_ShouldHandleNonStringValue(self):
        input = {'height': 1}
        with self.assertRaises(ValueError):
            adjust.extractHeight(input)
        self.assertEqual(input['error'], 'height is invalid')

    def test410_920_ShouldHandleNonNumericStringValue(self):
        input = {'height': 'abc'}
        with self.assertRaises(ValueError):
            adjust.extractHeight(input)
        self.assertEqual(input['error'], 'height is invalid')

    def test410_920_ShouldHandleNonNumericStringValue(self):
        input = {'height': '-1.0'}
        with self.assertRaises(ValueError):
            adjust.extractHeight(input)
        self.assertEqual(input['error'], 'height is invalid')

    # 420 extractObservation
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     sighting, a dictionary containing 'observation', which should be a string
    #                   representation of a non-negative numeric value.
    #       outputs:    the numeric value represented.
    #                   otherwise, sets the error field of the dictionary and raises value error.
    #   Happy Path:
    #       Nominal Value         '45d30.0'   -> 45.5
    #       The bulk of the testing for this is covered in tests 510 for degreeStringToDegrees
    #   Sad Path
    #       Non - String Value     'observation' : 20    -> 'error': 'observation is invalid', ValueError()
    #       No Value                NONE -> 'error': 'mandatory information is missing', ValueError()
    # Happy Path
    def test420_010_ShouldHandleNominalValue(self):
        input = {'observation': '45d30.0'}
        self.assertAlmostEqual(adjust.extractObservation(input), 45.5, 5)

    # Sad Paths
    def test420_910_ShouldHandleNonStringValue(self):
        input = {'observation': 20}
        with self.assertRaises(ValueError):
            adjust.extractObservation(input)
        self.assertEqual(input['error'], 'mandatory information is missing')
