import unittest
import softwareprocess.operations.predict as predict

class TestPredictAcceptance(unittest.TestCase):

     # 100 predict
    #   Desired level of confidence:    boundary value analysis
    #   Input-output Analysis:
    #       inputs:     sighting: dictionary containing 'op': 'predict', validated.
    #       outputs:    sighting passed, unchanged.
    #   Happy Path
    #       dictionary containing only op
    #       dictionary containing extra values
    #   Sad Path
    #       dictionary missing mandatory body field.
    #       dictionary with invalid body field (wrong type)
    #       dictionary with non-existent star field
    #       dictionary with invalid date field (wrong type)
    #       dictionary with invalid date field (improper format)
    #       dictionary with invalid time field (wrong type)
    #       dictionary with invalid time field (improper format)
    #       dictionary with lat field
    #       dictionary with long field
    #
    # Happy Path
    def test_100_010_ShouldPredictNominalValue(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42'}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42',
                    'long':'75d53.6', 'lat':'7d24.3'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should calculate latitude and longitude correctly')

    def test_100_020_ShouldPredictNominalValueWithAddedField(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'ignore': 'me'}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42',
                    'long':'75d53.6', 'lat':'7d24.3', 'ignore': 'me'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should calculate latitude and longitude correctly')

    # Sad Path
    def test_100_910_PredictShouldHandleMissingBody(self):
        test_input = {'op': 'predict'}
        expected = {'op': 'predict', 'error': 'mandatory information is missing'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify body field exists')

    def test_100_920_PredictShouldHandleWrongTypeBody(self):
        test_input = {'op': 'predict', 'body': 3}
        expected = {'op': 'predict', 'body': 3, 'error': 'invalid body'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify body exists')

    def test_100_930_PredictShouldHandleNonExistentBodyField(self):
        test_input = {'op': 'predict', 'body': 'unknown'}
        expected = {'op': 'predict', 'body': 'unknown', 'error': 'star not in catalog'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify body in catalog')

    def test_100_940_PredictShouldHandleWrongTypeDateField(self):
        test_input = {'op': 'predict', 'body': 'Betelgeuse', 'date': 15}
        expected = {'op': 'predict', 'body': 'Betelgeuse', 'date': 15, 'error': 'invalid date'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify date is string')

    def test_100_950_PredictShouldHandleWrongFormatDateField(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17'}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-99-17', 'error': 'invalid date'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify date format')

    def test_100_960_PredictShouldHandleWrongTypeTimeField(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 15}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': 15,
                    'error': 'invalid time'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify time is string')

    def test_100_970_PredictShouldHandleWrongFormatTimeField(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99'}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:99',
                    'error': 'invalid time'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify time format')

    def test_100_980_PredictShouldHandleLatInput(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'lat': '7d24.3'}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'lat': '7d24.3',
                    'error': 'lat key cannot be passed'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify lat is not passed')

    def test_100_980_PredictShouldHandleLongInput(self):
        test_input = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long': '7d24.3'}
        expected = {'op':'predict', 'body': 'Betelgeuse', 'date': '2016-01-17', 'time': '03:15:42', 'long': '7d24.3',
                    'error': 'long key cannot be passed'}
        actual = predict(test_input)
        self.assertEqual(actual, expected, 'Should verify long is not passed')
