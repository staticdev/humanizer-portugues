#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Time humanizing functions. These are largely borrowed from Django's
``contrib.humanize``."""

import time
from datetime import datetime, timedelta, date

__all__ = ['naturaldelta', 'naturaltime', 'naturalday', 'naturaldate', 'naturalyear']

MONTHS = {"Jan": "janeiro",
    "Feb": "fevereiro",
    "Mar": "março",
    "Apr": "abril",
    "May": "maio",
    "Jun": "junho",
    "Jul": "julho",
    "Aug": "agosto",
    "Sep": "setembro",
    "Sept": "setembro",
    "Oct": "outubro",
    "Nov": "novembro",
    "Dec": "dezembro"}

def _now():
    return datetime.now()

def abs_timedelta(delta):
    """Returns an "absolute" value for a timedelta, always representing a
    time distance."""
    if delta.days < 0:
        now = _now()
        return now - (now + delta)
    return delta

def date_and_delta(value):
    """Turn a value into a date and a timedelta which represents how long ago
    it was. If that's not possible, return (None, value)."""
    now = _now()
    if isinstance(value, datetime):
        date = value
        delta = now - value
    elif isinstance(value, timedelta):
        date = now - value
        delta = value
    else:
        try:
            value = int(value)
            delta = timedelta(seconds=value)
            date = now - delta
        except (ValueError, TypeError):
            return (None, value)
    return date, abs_timedelta(delta)

def naturaldelta(value, months=True):
    """Given a timedelta or a number of seconds, return a natural
    representation of the amount of time elapsed. This is similar to
    ``naturaltime``, but does not add tense to the result. If ``months``
    is True, then a number of months (based on 30.5 days) will be used
    for fuzziness between years."""
    now = _now()
    date, delta = date_and_delta(value)
    if date is None:
        return value

    use_months = months

    seconds = abs(delta.seconds)
    days = abs(delta.days)
    years = days // 365
    days = days % 365
    months = int(days // 30.5)

    if not years and days < 1:
        if seconds == 0:
            return "um momento"
        elif seconds == 1:
            return "um segundo"
        elif seconds < 60:
            return "%d segundos" % seconds
        elif 60 <= seconds < 120:
            return "um minuto"
        elif 120 <= seconds < 3600:
            minutes = seconds // 60
            return "%d minutos" % minutes
        elif 3600 <= seconds < 3600 * 2:
            return "uma hora"
        elif 3600 < seconds:
            hours = seconds // 3600
            return "%d horas" % hours
    elif years == 0:
        if days == 1:
            return "um dia"
        if not use_months:
            return "%d dias" % days
        else:
            if not months:
                return "%d dias" % days
            elif months == 1:
                return "um mês"
            else:
                return "%d meses" % months
    elif years == 1:
        if not months and not days:
            return "um ano"
        elif not months:
            return "1 ano e %d dias" % days
        elif use_months:
            if months == 1:
                return "1 ano e 1 mês"
            else:
                return "1 ano e %d meses" % months
        else:
            return "1 ano e %d dias" % days
    else:
        return "%d anos" % years


def naturaltime(value, future=False, months=True):
    """Given a datetime or a number of seconds, return a natural representation
    of that time in a resolution that makes sense. This is more or less
    compatible with Django's ``naturaltime`` filter. ``future`` is ignored for
    datetimes, where the tense is always figured out based on the current time.
    If an integer is passed, the return value will be past tense by default,
    unless ``future`` is set to True."""
    now = _now()
    date, delta = date_and_delta(value)
    if date is None:
        return value
    # determine tense by value only if datetime/timedelta were passed
    if isinstance(value, (datetime, timedelta)):
        future = date > now

    ago = 'em %s' if future else 'há %s'
    delta = naturaldelta(delta, months)

    if delta == "um momento":
        return "agora"

    return ago % delta

def naturalday(value, hasYear=False):
    """For date values that are tomorrow, today or yesterday compared to
    present day returns representing string. Otherwise, returns a string
    formatted according to ``format``."""
    try:
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't date-ish
        return value
    except (OverflowError, ValueError):
        # Date arguments out of range
        return value
    delta = value - date.today()
    if delta.days == 0:
        return 'hoje'
    elif delta.days == 1:
        return 'amanhã'
    elif delta.days == -1:
        return 'ontem'
    month = MONTHS[value.strftime('%b')]
    natday = 'em {0} de {1}'.format(value.strftime('%d'), month)
    if hasYear:
        natday += ' de {0}'.format(value.strftime('%Y'), )
    return natday

def naturalyear(value):
    """For date values that are last year, this year or next year compared to
    present year returns representing string. Otherwise, returns a string
    formatted according to the year."""
    try:
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't date-ish
        return value
    except (OverflowError, ValueError):
        # Date arguments out of range
        return value
    delta = value.year - date.today().year
    if delta == 0:
        return 'este ano'
    elif delta == 1:
        return 'ano que vem'
    elif delta == -1:
        return 'ano passado'
    return value.strftime('%Y')

def naturaldate(value):
    """Like naturalday, but will append a year for dates that are a year
    ago or more."""
    try:
        value = date(value.year, value.month, value.day)
    except AttributeError:
        # Passed value wasn't date-ish
        return value
    except (OverflowError, ValueError):
        # Date arguments out of range
        return value
    delta = abs_timedelta(value - date.today())
    if delta.days >= 365:
        return naturalday(value, True)
    return naturalday(value)
