#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Time humanizing functions.

These are largely borrowed from Django's ``contrib.humanize``.
"""
import datetime
from typing import Any
from typing import Tuple

__all__ = [
    "natural_clock",
    "natural_delta",
    "natural_time",
    "natural_day",
    "natural_date",
    "natural_year",
]

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
    12: "dezembro",
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
    23: "vinte e três",
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
    59: "cinquenta e nove",
}


def _now():
    return datetime.datetime.now()


def natural_period(hour):
    """Given current hour, returns period of the day."""
    if 0 < hour < 12:
        return "manhã"
    elif 12 < hour <= 18:
        return "tarde"
    elif 18 < hour <= 23:
        return "noite"
    return ""


def _formal_time(value, hour):
    clock = HOURS[hour]
    if hour in [0, 1]:
        clock += " hora"
    else:
        clock += " horas"
    if value.minute in [40, 45, 50, 55]:
        clock = MINUTES[60 - value.minute] + " minutos para " + clock
    elif value.minute == 1:
        clock += " e um minuto"
    elif value.minute != 0:
        clock += " e " + MINUTES[value.minute] + " minutos"
    return clock


def _informal_time(value, hour):
    clock = HOURS[hour]
    if hour == 0:
        clock = "meia noite"
    elif hour == 12:
        clock = "meio dia"
    if value.minute in [40, 45, 50, 55]:
        clock = MINUTES[60 - value.minute] + " para " + clock
    elif value.minute == 30:
        clock += " e meia"
    elif value.minute != 0:
        clock += " e " + MINUTES[value.minute]
    return clock


def natural_clock(value: Any, formal: bool = True) -> Any:
    """Returns human-readable time.

    Compares time values to present time returns representing readable of time
    with the given day period.

    Args:
        value (Any): any datetime.
        formal (bool): Formal or informal reading. Defaults to True.

    Returns:
        Any: readable time or original object.
    """
    try:
        time = datetime.time(value.hour, value.minute, value.second)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't time-ish or time arguments out of range
        return value
    if time.minute in [40, 45, 50, 55]:
        hour = time.hour + 1
    else:
        hour = time.hour

    period = natural_period(hour)

    if formal:
        clock = _formal_time(time, hour)
    else:
        if hour > 12:
            hour -= 12
        clock = _informal_time(time, hour)
        if period:
            clock += " da " + period

    return str(clock)


def abs_timedelta(delta: datetime.timedelta) -> datetime.timedelta:
    """Returns an "absolute" value for a timedelta.

    Args:
        delta (datetime.timedelta): relative timedelta.

    Returns:
        return (datetime.timedelta): absolute timedelta.
    """
    if delta.days < 0:
        now = _now()
        return now - (now + delta)
    return delta


def date_and_delta(value: Any) -> Tuple[Any, Any]:
    """Returns date and timedelta.

    Turn a value into a date and a timedelta which represents how long ago
    it was. If that's not possible, return (None, value).

    Args:
        value (Any): date value.

    Returns:
        Tuple[Any, Any]: date and delta or tuple of None, original value.
    """
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


def _less_than_a_day(seconds):
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
    hours = seconds // 3600
    return "%d horas" % hours


def _less_than_a_year(days, months, use_months):
    if days == 1:
        return "um dia"
    if not use_months:
        return "%d dias" % days
    if not months:
        return "%d dias" % days
    if months == 1:
        return "um mês"
    return "%d meses" % months


def _one_year(days, months, use_months):
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


def more_than_one_year(years: int) -> str:
    return "%d anos" % years


def natural_delta(value: Any, use_months: bool = True) -> Any:
    """Returns human-readable time difference.

    Given a timedelta or a number of seconds, return a natural
    representation of the amount of time elapsed. This is similar to
    ``natural_time``, but does not add tense to the result. If ``use_months``
    is True, then a number of months (based on 30.5 days) will be used
    for fuzziness between years.

    Args:
        value (Any): date.
        use_months (bool): show the number of months. Defaults to True.

    Returns:
        Any: time representation in natural language or original object.
    """
    date, delta = date_and_delta(value)
    if date is None:
        return value

    seconds = abs(delta.seconds)
    days = abs(delta.days)
    years = days // 365
    days = days % 365
    months = int(days // 30.5)

    if not years and days < 1:
        return _less_than_a_day(seconds)
    elif years == 0:
        return _less_than_a_year(days, months, use_months)
    elif years == 1:
        return _one_year(days, months, use_months)
    return more_than_one_year(years)


def natural_time(value: Any, future: bool = False, use_months: bool = True) -> Any:
    """Returns human-readable time.

    Given a datetime or a number of seconds, return a natural representation
    of that time in a resolution that makes sense. This is more or less
    compatible with Django's ``natural_time`` filter. ``future`` is ignored for
    datetimes, where the tense is always figured out based on the current time.
    If an integer is passed, the return value will be past tense by default,
    unless ``future`` is set to True.

    Args:
        value (Any): time value.
        future (bool): if false uses past tense. Defaults to False.
        use_months (bool): if true return number of months. Defaults to True.

    Returns:
        Any: time in natural language or original object.
    """
    now = _now()
    date, delta = date_and_delta(value)
    if date is None:
        return value
    # determine tense by value only if datetime/timedelta were passed
    if isinstance(value, (datetime.datetime, datetime.timedelta)):
        future = date > now

    ago = "em %s" if future else "há %s"
    delta = natural_delta(delta, use_months)

    if delta == "um momento":
        return "agora"

    return ago % delta


def natural_day(value: Any, has_year: bool = False) -> Any:
    """Returns human-readable day.

    For date values that are tomorrow, today or yesterday compared to
    present day returns representing string. Otherwise, returns a string
    formatted according to ``format``.

    Args:
        value (Any): a date.
        has_year (bool): if year is added. Defaults to False.

    Returns:
        Any: date formatted in natural language or original object.
    """
    try:
        date = datetime.date(value.year, value.month, value.day)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't date-ish or date arguments out of range
        return value
    delta = date - datetime.date.today()
    if delta.days == 0:
        return "hoje"
    if delta.days == 1:
        return "amanhã"
    if delta.days == -1:
        return "ontem"
    month = MONTHS[date.month]
    natday = "{0} de {1}".format(date.day, month)
    if has_year:
        natday += " de {0}".format(date.year)
    return natday


def natural_year(value: Any) -> Any:
    """Returns human-readable year.

    For date values that are last year, this year or next year compared to
    present year returns representing string. Otherwise, returns a string
    formatted according to the year.

    Args:
        value: a date.

    Returns:
        Any: year in natural language or original object.
    """
    try:
        date = datetime.date(value.year, value.month, value.day)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't date-ish or date arguments out of range
        return value
    delta = date.year - datetime.date.today().year
    if delta == 0:
        return "este ano"
    if delta == 1:
        return "ano que vem"
    if delta == -1:
        return "ano passado"
    return str(date.year)


def natural_date(value: Any) -> Any:
    """Returns human-readable date.

    Like natural_day, but will append a year for dates that are a year
    ago or more.

    Args:
        value: a date.

    Returns:
        Any: date in natural language or original object.
    """
    try:
        date = datetime.date(value.year, value.month, value.day)
    except (AttributeError, OverflowError, ValueError):
        # Passed value wasn't date-ish or date arguments out of range
        return value
    delta = abs_timedelta(date - datetime.date.today())
    if delta.days >= 365:
        return natural_day(date, True)
    return natural_day(date)
