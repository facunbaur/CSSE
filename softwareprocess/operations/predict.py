"""
    predict.py contains functionality for the 'predict' operation
    to be used in star simulation calculations.

    Created on 3/20/2017
    Last Modified on 3/20/2017

    @author: Mitchell Price
"""
import datetime

star_data = {
    'alpheratz': {'sha': '357d41.7', 'declination': '29d10.9'},
    'ankaa': {'sha': '353d14.1', 'declination': '-42d13.4'},
    'schedar': {'sha': '349d38.4', 'declination': '56d37.7'},
    'diphda': {'sha': '348d54.1', 'declination': '-17d54.1'},
    'achernar': {'sha': '335d25.5', 'declination': '-57d09.7'},
    'hamal': {'sha': '327d58.7', 'declination': '23d32.3'},
    'polaris': {'sha': '316d41.3', 'declination': '89d20.1'},
    'akamar': {'sha': '315d16.8', 'declination': '-40d14.8'},
    'menkar': {'sha': '314d13.0', 'declination': '4d09.0'},
    'mirfak': {'sha': '308d37.4', 'declination': '49d55.1'},
    'aldebaran': {'sha': '290d47.1', 'declination': '16d32.3'},
    'rigel': {'sha': '281d10.1', 'declination': '-8d11.3'},
    'capella': {'sha': '280d31.4', 'declination': '46d00.7'},
    'bellatrix': {'sha': '278d29.8', 'declination': '6d21.6'},
    'elnath': {'sha': '278d10.1', 'declination': '28d37.1'},
    'alnilam': {'sha': '275d44.3', 'declination': '-1d11.8'},
    'betelgeuse': {'sha': '270d59.1', 'declination': '7d24.3'},
    'canopus': {'sha': '263d54.8', 'declination': '-52d42.5'},
    'sirius': {'sha': '258d31.7', 'declination': '-16d44.3'},
    'adara': {'sha': '255d10.8', 'declination': '-28d59.9'},
    'procyon': {'sha': '244d57.5', 'declination': '5d10.9'},
    'pollux': {'sha': '243d25.2', 'declination': '27d59.0'},
    'avior': {'sha': '234d16.6', 'declination': '-59d33.7'},
    'suhail': {'sha': '222d50.7', 'declination': '-43d29.8'},
    'miaplacidus': {'sha': '221d38.4', 'declination': '-69d46.9'},
    'alphard': {'sha': '217d54.1', 'declination': '-8d43.8'},
    'regulus': {'sha': '207d41.4', 'declination': '11d53.2'},
    'dubhe': {'sha': '193d49.4', 'declination': '61d39.5'},
    'denebola': {'sha': '182d31.8', 'declination': '14d28.9'},
    'gienah': {'sha': '175d50.4', 'declination': '-17d37.7'},
    'acrux': {'sha': '173d07.2', 'declination': '-63d10.9'},
    'gacrux': {'sha': '171d58.8', 'declination': '-57d11.9'},
    'alioth': {'sha': '166d19.4', 'declination': '55d52.1'},
    'spica': {'sha': '158d29.5', 'declination': '-11d14.5'},
    'alcaid': {'sha': '152d57.8', 'declination': '49d13.8'},
    'hadar': {'sha': '148d45.5', 'declination': '-60d26.6'},
    'menkent': {'sha': '148d05.6', 'declination': '-36d26.6'},
    'arcturus': {'sha': '145d54.2', 'declination': '19d06.2'},
    'rigil kent.': {'sha': '139d49.6', 'declination': '-60d53.6'},
    'zubenelg.': {'sha': '137d03.7', 'declination': '-16d06.3'},
    'kochab': {'sha': '137d21.0', 'declination': '74d05.2'},
    'alphecca': {'sha': '126d09.9', 'declination': '26d39.7'},
    'antares': {'sha': '112d24.4', 'declination': '-26d27.8'},
    'atria': {'sha': '107d25.2', 'declination': '-69d03.0'},
    'sabik': {'sha': '102d10.9', 'declination': '-15d44.4'},
    'shaula': {'sha': '96d20.0', 'declination': '-37d06.6'},
    'rasalhague': {'sha': '96d05.2', 'declination': '12d33.1'},
    'etamin': {'sha': '90d45.9', 'declination': '51d29.3'},
    'kaus aust.': {'sha': '83d41.9', 'declination': '-34d22.4'},
    'vega': {'sha': '80d38.2', 'declination': '38d48.1'},
    'nunki': {'sha': '75d56.6', 'declination': '-26d16.4'},
    'altair': {'sha': '62d06.9', 'declination': '8d54.8'},
    'peacock': {'sha': '53d17.2', 'declination': '-56d41.0'},
    'deneb': {'sha': '49d30.7', 'declination': '45d20.5'},
    'enif': {'sha': '33d45.7', 'declination': '9d57.0'},
    'alnair': {'sha': '27d42.0', 'declination': '-46d53.1'},
    'fomalhaut': {'sha': '15d22.4', 'declination': '-29d32.3'},
    'scheat': {'sha': '13d51.8', 'declination': '28d10.3'},
    'markab': {'sha': '13d36.7', 'declination': '15d17.6'}
}

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
    In the event that there is no valid body field in the input, it will add an 'error' field
    containing a diagnostic string.
    :param sighting: A dictionary containing data on a star sighting.
    :return: A dictionary mapping 'sha' to the star's SHA, and 'declination' to the start's Declination.
    """
    if not 'body' in sighting:
        sighting['error'] = 'mandatory information is missing'
        return None
    star = sighting['body']
    if not isinstance(star, basestring):
        sighting['error'] = 'invalid body'
        return None
    star = star.lower()
    if star not in star_data:
        sighting['error'] = 'star not in catalog'
        return None
    return star_data[star]

def extractDate(sighting):
    """
    extractDate will attempt to extract the date field from the given sighting.
    In the event that there is no key 'date', the default value will be returned.
    In the event that the value for the 'date' key is invalid, an error field will be added containing a
    diagnostic string. Otherwise, this will return a timedate.date value matching the string, which should
    be of the format: yyyy-mm-dd, where yyyy is >= 2001
    :param sighting: A dictionary containing data on a star sighting.
    :return: A datetime.date containing the date of the sighting.
    """
    if 'date' not in sighting:
        return datetime.date(2001, 01, 01)
    dateStr = sighting['date']
    if not isinstance(dateStr, basestring):
        sighting['error'] = 'invalid date'
        return None
    fields = dateStr.split('-')
    if not len(fields) == 3:
        sighting['error'] = 'invalid date'
        return None
    try:
        date = datetime.date(int(fields[0]), int(fields[1]), int(fields[2]))
    except Exception:
        sighting['error'] = 'invalid date'
        return None
    if date.year < 2001:
        sighting['error'] = 'invalid date'
        return None
    return date

def extractTime(sighting):
    """
    extractTime will attempt to extract the time field from the given sighting.
    In the event that there is no key 'time', the default value will be returned.
    In the event that the value for the 'time' key is invalid, an error field will be added containing a
    diagnostic string. Otherwise, this will return a timedate.time value matching the string, which should be
    of the format: hh-mm-ss
    :param sighting: A dictionary containing date on a star sighting.
    :return: A datetime.time containing the time of the sighting.
    """
    if 'time' not in sighting:
        return datetime.time(0, 0, 0)
    timeStr = sighting['time']
    if not isinstance(timeStr, basestring):
        sighting['error'] = 'invalid time'
        return None
    fields = timeStr.split(':')
    return datetime.time(int(fields[0]), int(fields[1]), int(fields[2]))
