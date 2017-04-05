"""
    predict.py contains functionality for the 'predict' operation
    to be used in star simulation calculations.

    Created on 3/20/2017
    Last Modified on 3/20/2017

    @author: Mitchell Price
"""


def predict(sighting):
    """
    Stub for the predict operation.
    :param sighting: A dictionary containing data on a star sighting.
    :return: The unmodified sighting.
    """
    return sighting

def extractBody(sighting):
    """
    extractBody will attempt to extract the body field from the given sighting.
    In the event that there is no valid body field in the input, it will raise a value
    error containing a diagnostic string.
    :param sighting: A dictionary containing data on a star sighting.
    :return: A dictionary mapping 'sha' to the star's SHA, and 'declination' to the start's Declination.
    """
    pass

def extractDate(sighting):
    """
    extractDate will attempt to extract the date field from the given sighting.
    In the event that there is no key 'date', the default value will be returned.
    In the event that the value for the 'date' key is invalid, a ValueError will be raised with a
    diagnostic string. Otherwise, this will return a timedate.date value matching the string, which should
    be of the format: yyyy-mm-dd, where yyyy is >= 2001
    :param sighting: A dictionary containing data on a star sighting.
    :return: A datetime.date containing the date of the sighting.
    """
    pass

def extractTime(sighting):
    """
    extractTime will attempt to extract the time field from the given sighting.
    In the event that there is no key 'time', the default value will be returned.
    In the event that the value for the 'time' key is invalid, a ValueError will be raised with a
    diagnostic string. Otherwise, this will return a timedate.time value matching the string, which should be
    of the format: hh-mm-ss
    :param sighting: A dictionary containing date on a star sighting.
    :return: A datetime.time containing the time of the sighting.
    """
    pass
