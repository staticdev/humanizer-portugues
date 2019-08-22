#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Time humanizing functions. These are largely borrowed from Django's
``contrib.humanize``."""

import datetime

__all__ = ['naturalclock', 'naturaldelta', 'naturaltime',
           'naturalday', 'naturaldate', 'naturalyear']

MONTHS = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}

HOURS = {
    0: "zero",
    1: "uma",
    2: "duas",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
    21: "vinte e uma",
    22: "vinte e duas",
    23: "vinte e três"
}

MINUTES = {
    1: "um",
    2: "dois",
    3: "três",
    4: "quatro",
    5: "cinco",
    6: "seis",
    7: "sete",
    8: "oito",
    9: "nove",
    10: "dez",
    11: "onze",
    12: "doze",
    13: "treze",
    14: "quatorze",
    15: "quinze",
    16: "dezesseis",
    17: "dezessete",
    18: "dezoito",
    19: "dezenove",
    20: "vinte",
    21: "vinte e um",
    22: "vinte e dois",
    23: "vinte e três",
    24: "vinte e quatro",
    25: "vinte e cinco",
    26: "vinte e seis",
    27: "vinte e sete",
    28: "vinte e oito",
    29: "vinte e nove",
    30: "trinta",
    31: "trinta e um",
    32: "trinta e dois",
    33: "trinta e três",
    34: "trinta e quatro",
    35: "trinta e cinco",
    36: "trinta e seis",
    37: "trinta e sete",
    38: "trinta e oito",
    39: "trinta e nove",
    40: "quarenta",
    41: "quarenta e um",
    42: "quarenta e dois",
    43: "quarenta e três",
    44: "quarenta e quatro",
    45: "quarenta e cinco",
    46: "quarenta e seis",
    47: "quarenta e sete",
    48: "quarenta e oito",
    49: "quarenta e nove",
    50: "cinquenta",
    51: "cinquenta e um",
    52: "cinquenta e dois",
    53: "cinquenta e três",
    54: "cinquenta e quatro",
    55: "cinquenta e cinco",
    56: "cinquenta e seis",
    57: "cinquenta e sete",
    58: "cinquenta e oito",
    59: "cinquenta e nove"
}


def _now():
    return datetime.datetime.now()


def naturalclock(value, formal=True):
    """Compares time values to present time
    returns representing readable of time with the given day period."""
    try:
        value = datetime.time(value.hour, value.minute, value.second)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't time-ish or time arguments out of range
        return value
    if value.minute in [40, 45, 50, 55]:
        used_hour = value.hour + 1
    else:
        used_hour = value.hour
    if 0 < used_hour <= 11:
        period = 'manhã'
    elif 12 < used_hour <= 18:
        period = 'tarde'
    elif 18 < used_hour <= 23:
        period = 'noite'
    # Formal time
    if formal:
        clock = HOURS[used_hour]
        if used_hour in [0, 1]:
            clock += ' hora'
        else:
            clock += ' horas'
        if value.minute in [40, 45, 50, 55]:
            clock = MINUTES[60 - value.minute] + ' minutos para ' + clock
        elif value.minute == 1:
            clock += ' e um minuto'
        elif value.minute != 0:
            clock += ' e ' + MINUTES[value.minute] + ' minutos'
    # Informal time
    else:
        if used_hour > 12:
            used_hour -= 12
        clock = HOURS[used_hour]

        if used_hour == 0:
            clock = 'meia noite'
        elif used_hour == 12:
            clock = 'meio dia'
        if value.minute in [40, 45, 50, 55]:
            clock = MINUTES[60 - value.minute] + ' para ' + clock
        elif value.minute == 30:
            clock += ' e meia'
        elif value.minute != 0:
            clock += ' e ' + MINUTES[value.minute]
        try:
            clock += ' da ' + period
        except UnboundLocalError:
            pass
    return str(clock)


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
    if isinstance(value, datetime.datetime):
        date = value
        delta = now - value
    elif isinstance(value, datetime.timedelta):
        date = now - value
        delta = value
    else:
        try:
            value = int(value)
            delta = datetime.timedelta(seconds=value)
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
        if seconds == 1:
            return "um segundo"
        if seconds < 60:
            return "%d segundos" % seconds
        if 60 <= seconds < 120:
            return "um minuto"
        if 120 <= seconds < 3600:
            minutes = seconds // 60
            return "%d minutos" % minutes
        if 3600 <= seconds < 3600 * 2:
            return "uma hora"
        if seconds > 3600:
            hours = seconds // 3600
            return "%d horas" % hours
    elif years == 0:
        if days == 1:
            return "um dia"
        if not use_months:
            return "%d dias" % days
        if not months:
            return "%d dias" % days
        if months == 1:
            return "um mês"
        return "%d meses" % months
    elif years == 1:
        if not months and not days:
            return "um ano"
        if not months:
            if days == 1:
                return "1 ano e 1 dia"
            return "1 ano e %d dias" % days
        if use_months:
            if months == 1:
                return "1 ano e 1 mês"
            return "1 ano e %d meses" % months
        return "1 ano e %d dias" % days
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
    if isinstance(value, (datetime.datetime, datetime.timedelta)):
        future = date > now

    ago = 'em %s' if future else 'há %s'
    delta = naturaldelta(delta, months)

    if delta == "um momento":
        return "agora"

    return ago % delta


def naturalday(value, has_year=False):
    """For date values that are tomorrow, today or yesterday compared to
    present day returns representing string. Otherwise, returns a string
    formatted according to ``format``."""
    try:
        value = datetime.date(value.year, value.month, value.day)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't date-ish or date arguments out of range
        return value
    delta = value - datetime.date.today()
    if delta.days == 0:
        return 'hoje'
    if delta.days == 1:
        return 'amanhã'
    if delta.days == -1:
        return 'ontem'
    month = MONTHS[value.month]
    natday = '{0} de {1}'.format(value.day, month)
    if has_year:
        natday += ' de {0}'.format(value.year)
    return natday


def naturalyear(value):
    """For date values that are last year, this year or next year compared to
    present year returns representing string. Otherwise, returns a string
    formatted according to the year."""
    try:
        value = datetime.date(value.year, value.month, value.day)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't date-ish or date arguments out of range
        return value
    delta = value.year - datetime.date.today().year
    if delta == 0:
        return 'este ano'
    if delta == 1:
        return 'ano que vem'
    if delta == -1:
        return 'ano passado'
    return str(value.year)


def naturaldate(value):
    """Like naturalday, but will append a year for dates that are a year
    ago or more."""
    try:
        value = datetime.date(value.year, value.month, value.day)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't date-ish or date arguments out of range
        return value
    delta = abs_timedelta(value - datetime.date.today())
    if delta.days >= 365:
        return naturalday(value, True)
    return naturalday(value)
