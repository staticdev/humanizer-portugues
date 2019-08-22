#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Lists related humanization."""

__all__ = ['naturallist']


def naturallist(itens, separator, conjunction=None):
    """
    Returns human readable list separated by separator
    Optional argument is conjuntion that substitutes the last separator
    """
    len_itens = len(itens)
    if len_itens == 0:
        return ''
    if len_itens == 1:
        return itens[0]
    phrase = itens[0]
    if conjunction:
        for i in range(1, len_itens - 1):
            phrase += '%s %s' % (separator, itens[i])
        phrase += ' %s %s' % (conjunction, itens[len_itens - 1])
    else:
        for i in range(1, len_itens):
            phrase += '%s %s' % (separator, itens[i])
    return phrase
