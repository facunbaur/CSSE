import math


def degreeStringToDegrees(degreeString, validate=True):
    """
    Takes a string format of a degree measurement and produces the corresponding numeric value.
    :param degreeString: String, of the format '<x>d<y>', where x is an integer from 0 to 89,
    the number of degrees, and y is a numeric value, between 0 and 60, the number of minutes.
    :param validate: Boolean (optional, default True). If true, will ensure that the measurement is in (0, 90)
    :return: x + (y / 60), or will raise a value error if the given string is not formatted properly.
    """
    if degreeString.count('d') == 0:
        raise ValueError("No 'd' delimiter")
    elif degreeString.count('d') > 1:
        raise ValueError("Too many 'd' delimiters")
    dIndex = degreeString.index('d')
    if degreeString[0] == '-':
        degrees = int(degreeString[1:dIndex])
    else:
        degrees = int(degreeString[:dIndex])
    minutes = float(degreeString[dIndex+1:])
    if minutes < 0:
        raise ValueError("Negative number of minutes")
    elif minutes >= 60.0:
        raise ValueError("Number of minutes too large")
    value = degrees + (minutes / 60)
    if degreeString[0] == '-':
        value = -value
    if value < 0.1 / 60 and validate:
        raise ValueError("Measurement too small")
    elif value >= 90.0 and validate:
        raise ValueError("Measurement too large")
    return value


def degreesToDegreeString(degrees):
    """
    Takes an arc measurement and produces the corresponding degree / minute string representation,
    of the form '<x>d<y>', where x is the number of degrees, and y is the number of minutes.
    :param degrees: Numeric, an arc measurement.
    :return: The string representation of the degrees and minutes in the arc.
    """
    x = math.floor(degrees)
    y = (degrees - x) * 60
    return "%dd%0.1f" % (x, y)
