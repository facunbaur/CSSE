"""
    correct.py contains functionality for the 'correct' operation
    to be used in star simulation calculations.

    Created on 3/20/2017
    Last Modified on 3/20/2017

    @author: Mitchell Price
"""
import math
from util import degreeStringToDegrees, degreesToDegreeString


def correct(sighting):
    """
    Stub for the correct operation.
    :param sighting: A dictionary containing data on a star sighting.
    :return: The unmodified sighting.
    """
    try:
        lat = extractMeasurement(sighting, "lat", -90, 90)
    except:
        return sighting

    try:
        lon = extractMeasurement(sighting, "long", 0, 360)
    except:
        return sighting

    try:
        altitude = extractMeasurement(sighting, "altitude", 0, 90)
    except:
        return sighting

    try:
        assumedLat = extractMeasurement(sighting, "assumedLat", -90, 90)
    except:
        return sighting

    try:
        assumedLon = extractMeasurement(sighting, "assumedLong", 0, 360)
    except:
        return sighting

    return sighting

def extractMeasurement(sighting, name, lowBound, highBound):
    if name not in sighting:
        sighting['error'] = 'missing mandatory field ' + name
        raise ValueError()
    elif not isinstance(sighting[name], basestring):
        sighting['error'] =  name + 'is invalid'
        raise ValueError()
    try:
        measurement = degreeStringToDegrees(sighting[name], False)
    except ValueError:
        sighting['error'] = name + ' is invalid'
        raise ValueError()
    if measurement < lowBound or measurement > highBound:
        sighting['error'] = name + ' is invalid'
        raise ValueError()
    return measurement

def calculateCorrectedDistance(lat, assumedLat, altitude, lon, assumedLon):
    intermediate = calculateIntermediateDistance(lat, assumedLat, lon, assumedLon)
    correctedAltitude = math.asin(intermediate)
    dist = math.degrees(math.radians(altitude) - correctedAltitude) * 60
    return round(dist)

def calculateCorrectedAzimuth():
    pass

def calculateIntermediateDistance(lat, assumedLat, lon, assumedLon):
    lha = math.radians(lon + assumedLon)
    latr = math.radians(lat)
    assumedLatr = math.radians(assumedLat)
    return (math.sin(latr) * math.sin(assumedLatr)) + (
        math.cos(latr) * math.cos(assumedLatr) * math.cos(lha))
