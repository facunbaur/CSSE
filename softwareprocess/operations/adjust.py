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
