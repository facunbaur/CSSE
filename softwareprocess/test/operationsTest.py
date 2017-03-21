import unittest
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
