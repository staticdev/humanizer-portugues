#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Lists related humanization."""
from typing import List

__all__ = ["natural_list"]


def natural_list(items: List[str], separator: str, conjunction: str = "") -> str:
    """Returns human readable list separated by separator.

    Optional argument is conjuntion that substitutes the last separator.

    Args:
        items (List): list of items.
        separator (str): separator of items.
        conjunction (str): word/string as last separator. Defaults to None.

    Returns:
        str: list in natural language.
    """
    len_items = len(items)
    if len_items == 0:
        return ""
    if len_items == 1:
        return items[0]
    phrase = items[0]
    if conjunction:
        for i in range(1, len_items - 1):
            phrase += "%s %s" % (separator, items[i])
        phrase += " %s %s" % (conjunction, items[len_items - 1])
    else:
        for i in range(1, len_items):
            phrase += "%s %s" % (separator, items[i])
    return phrase
