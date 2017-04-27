"""
    adjust.py contains functionality for the 'adjust' operation
    to be used in star simulation calculations.

    Created on 3/20/2017
    Last Modified on 3/20/2017

    @author: Mitchell Price
"""

import math

from util import degreeStringToDegrees, degreesToDegreeString


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
    if 'altitude' in sighting:
        sighting['error'] = 'altitude cannot be given in input'
        return sighting
    try:
        observation = extractObservation(sighting)
        height = extractHeight(sighting)
        temperature = extractTemperature(sighting)
        pressure = extractPressure(sighting)
        naturalHorizon = extractNaturalHorizon(sighting)
    except ValueError:
        return sighting
    altitude = degreesToDegreeString(calculateAltitude(observation, height, temperature, pressure, naturalHorizon))
    sighting['altitude'] = altitude
    return sighting


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
    dip = 0
    if naturalHorizon:
        dip = (-0.97 * math.sqrt(height)) / 60.0
    refraction = (-0.00452 * pressure) / (273 + fahrenheitToCelsius(temperature)) / \
                 math.tan(math.radians(observation))
    return observation + dip + refraction

def fahrenheitToCelsius(temp):
    return (temp - 32.0) * 5.0/9.0


def extractHeight(sighting):
    """
    Takes a star sighting and attempts to determine the height at which the observation was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, a numeric value, the height at which the observation was taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    if 'height' not in sighting:
        return 0.0
    elif not isinstance(sighting['height'], basestring):
        sighting['error'] = 'height is invalid'
        raise ValueError()
    try:
        height = float(sighting['height'])
    except ValueError:
        sighting['error'] = 'height is invalid'
        raise ValueError()
    if height < 0:
        sighting['error'] = 'height is invalid'
        raise ValueError()
    return height


def extractObservation(sighting):
    """
    Takes a star sighting and attempts to determine the observation that was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, a numeric value, the observation taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    if 'observation' not in sighting:
        sighting['error'] = 'mandatory information is missing'
        raise ValueError()
    elif not isinstance(sighting['observation'], basestring):
        sighting['error'] = 'observation is invalid'
        raise ValueError()

    try:
        return degreeStringToDegrees(sighting['observation'])
    except ValueError:
        sighting['error'] = 'observation is invalid'
        raise ValueError()



def extractTemperature(sighting):
    """
    Takes a star sighting and attempts to determine the temperature at which the observation was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, an integer value, the temperature at which the observation was taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    if 'temperature' not in sighting:
        return 72
    elif not isinstance(sighting['temperature'], basestring):
        sighting['error'] = 'temperature is invalid'
        raise ValueError()

    try:
        temperature = int(sighting['temperature'])
    except ValueError:
        sighting['error'] = 'temperature is invalid'
        raise ValueError()
    if temperature < -20 or temperature > 120:
        sighting['error'] = 'temperature is invalid'
        raise ValueError()
    return temperature


def extractPressure(sighting):
    """
    Takes a star sighting and attempts to determine the pressure at which the observation was made.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, an integer value, the pressure at which the observation was taken.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    if 'pressure' not in sighting:
        return 1010
    elif not isinstance(sighting['pressure'], basestring):
        sighting['error'] = 'pressure is invalid'
        raise ValueError()

    try:
        pressure = int(sighting['pressure'])
    except ValueError:
        sighting['error'] = 'pressure is invalid'
        raise ValueError()
    if pressure < 100 or pressure > 1100:
        sighting['error'] = 'pressure is invalid'
        raise ValueError()
    return pressure


def extractNaturalHorizon(sighting):
    """
    Takes a star sighting and attempts to determine whether the observation was made on a natural or artificial horizon.
    :param sighting: A dictionary containing information about a star sighting.
    :return: If input is valid, a boolean value, indicating if the observation was made on a natural horizon.
    Otherwise, the sighting's error field will be set accordingly, and a ValueError will be raised.
    """
    if not 'horizon' in sighting:
        return True
    elif not isinstance(sighting['horizon'], basestring):
        sighting['error'] = 'horizon is invalid'
        raise ValueError()

    horizon = sighting['horizon'].lower()
    if horizon == 'natural':
        return True
    elif horizon == 'artificial':
        return False
    else:
        sighting['error'] = 'horizon is invalid'
        raise ValueError()
