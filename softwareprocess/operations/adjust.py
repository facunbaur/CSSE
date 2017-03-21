"""
    adjust.py contains functionality for the 'adjust' operation
    to be used in star simulation calculations.

    Created on 3/20/2017
    Last Modified on 3/20/2017

    @author: Mitchell Price
"""


def adjust(sighting):
    """
    Implementation of the sighting operation. This operation is responsible for
    converting an observation, height, temperature, pressure, and horizon type
    into an altitude.
    :param sighting: A dictionary, containing the following fields:
        'observation' - Mandatory - an observation in degree/minutes string format. '0d0.1' <= observation < '90d0.0'
        'height' - Optional (default '0'), string of a numeric value. '0' <= height
        'temperature' - Optional (default '72'), string of an integer value. '-20' <= temperature <= '120'
        'pressure' - Optional (default '1010'), string of an integer value. '100' <= pressure <= '1100'
        'horizon' - Optional (default 'natural') case-insensitive string. Either 'natural' or 'artificial'.
    :return: The same dictionary, with one of two possible fields added:
        'altitude' - In the event of a success, the altitude corresponding to this sighting. Degrees/minutes string.
        'error' - In the event of an error, a string explaining the source of the error.
    """
    pass


def calculateAltitude(observation, height, temperature, pressure, naturalHorizon):
    """
    calculateAltitude is responsible for calculating the altitude given all
    parameters in an observation.
    :param observation: Numeric, the degrees of the observation.
    :param height: Numeric, the height at which the observation was taken.
    :param temperature: Integer, the temperature at which the observation was taken.
    :param pressure: Integer, the pressure at which the observation was taken.
    :param naturalHorizon: Boolean, True iff the horizon used was natural.
    :return: Numeric, the altitude (in degrees) of the star, after adjustment.
    """
    pass


def degreeStringToDegrees(degreeString):
    """
    Takes a string format of a degree measurement and produces the corresponding numeric value.
    :param degreeString: String, of the format '<x>d<y>', where x is an integer from 0 to 89,
    the number of degrees, and y is a numeric value, between 0 and 60, the number of minutes.
    :return: x + (y / 60), or will raise a value error if the given string is not formatted properly.
    """
    pass


def degreesToDegreeString(degrees):
    """
    Takes an arc measurement and produces the corresponding degree / minute string representation,
    of the form '<x>d<y>', where x is the number of degrees, and y is the number of minutes.
    :param degrees: Numeric, an arc measurement.
    :return: The string representation of the degrees and minutes in the arc.
    """
    pass


def extractHeight(sighting):
    """
    Takes a star sighting and attempts to determine the height at which the observation was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, a numeric value, the height at which the observation was taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    pass


def extractObservation(sighting):
    """
    Takes a star sighting and attempts to determine the observation that was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, a numeric value, the observation taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    pass


def extractTemperature(sighting):
    """
    Takes a star sighting and attempts to determine the temperature at which the observation was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, an integer value, the temperature at which the observation was taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    pass


def extractPressure(sighting):
    """
    Takes a star sighting and attempts to determine the pressure at which the observation was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, an integer value, the pressure at which the observation was taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    pass


def extractNaturalHorizon(sighting):
    """
    Takes a star sighting and attempts to determine whether the observation was made on a natural or artificial horizon.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, a boolean value, indicating if the observation was made on a natural horizon.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    pass