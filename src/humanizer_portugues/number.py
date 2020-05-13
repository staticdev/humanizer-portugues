#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Humanizing functions for numbers."""
import fractions
import re
from typing import Any


def ordinal(value: Any) -> Any:
    """Converts an integer to its ordinal as a string.

    1 is '1º', 2 is '2º', 3 is '3º', etc.
    Works for any integer or anything int() will turn into an integer.
    Anything other value will have nothing done to it.

    Args:
        value: integer.

    Returns:
        Any: ordinal string.
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value
    return "{}{}".format(value, "º")


def int_comma(value: Any) -> Any:
    """Converts an integer to a string containing commas every three digits.

    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.  To maintain
    some compatability with Django's int_comma, this function also accepts
    floats.

    Args:
        value: any number.

    Returns:
        Any: formatted number with commas.
    """
    try:
        if isinstance(value, str):
            float(value.replace(",", ""))
        else:
            float(value)
    except (TypeError, ValueError):
        return value
    orig = str(value)
    new = re.sub(r"^(-?\d+)(\d{3})", r"\g<1>,\g<2>", orig)
    if orig == new:
        return new
    return int_comma(new)


POWERS = [10 ** x for x in (6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 100)]
HUMAN_POWERS = (
    "milhão",
    "bilhão",
    "trilhão",
    "quatrilhão",
    "quintilhão",
    "sextilhão",
    "septilhão",
    "octilhão",
    "nonilhão",
    "decilhão",
    "googol",
)


def int_word(value: Any, formatting: str = "%.1f") -> Any:
    """Converts a large integer to a friendly text representation.

    Works best for numbers over 1 million.
    For example, 1000000 becomes '1.0 million', 1200000 becomes
    '1.2 million' and '1200000000' becomes '1.2 billion'.
    Supports up to decillion (33 digits) and googol (100 digits).
    You can pass format to change the number of decimal or general
    format of the number portion.
    This function returns a string unless the value passed was unable to be
    coaxed into an int.

    Args:
        value: any number.
        formatting (str): string formatting pattern. Defaults to "%.1f":str.

    Returns:
        Any: number formatted with scale words.
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value

    if value < POWERS[0]:
        return str(value)
    for ordin, power in enumerate(POWERS[1:], 1):
        if value < power:
            chopped = value / float(POWERS[ordin - 1])
            return (" ".join([formatting, HUMAN_POWERS[ordin - 1]])) % chopped
    return str(value)


def ap_number(value: Any) -> Any:
    """For numbers 1-9, returns the number spelled out. Otherwise, returns the number.

    This follows Associated Press style.  This always returns a string
    unless the value was not int-able, unlike the Django filter.

    Args:
        value: any number.

    Returns:
        Any: spelled 1-9 numbers or original number.
    """
    try:
        value = int(value)
    except (TypeError, ValueError):
        return value
    if not 0 < value < 10:
        return str(value)
    return ("um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")[
        value - 1
    ]


def fractional(value: Any) -> Any:
    """Returns a human readable fractional number.

    The return can be in the form of fractions and mixed fractions.
    There will be some cases where one might not want to show ugly decimal
    places for floats and decimals.

    Pass in a string, or a number or a float, and this function returns
        a string representation of a fraction
        or whole number
        or a mixed fraction

    Examples:
        fractional(0.3) will return '1/3'
        fractional(1.3) will return '1 3/10'
        fractional(float(1/3)) will return '1/3'
        fractional(1) will return '1'

    This will always return a string.

    Args:
        value: a number.

    Returns:
        Any: human readable number.
    """
    try:
        number = float(value)
    except (TypeError, ValueError):
        return value
    whole_number = int(number)
    frac = fractions.Fraction(number - whole_number).limit_denominator(1000)
    numerator = frac.numerator
    denominator = frac.denominator
    if whole_number and not numerator and denominator == 1:
        # this means that an integer was passed in
        # or variants of that integer like 1.0000
        return "%.0f" % whole_number
    if not whole_number:
        return "%.0f/%.0f" % (numerator, denominator)
    return "%.0f %.0f/%.0f" % (whole_number, numerator, denominator)
