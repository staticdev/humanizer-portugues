#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['naturallist']

SPACE = ' '

def naturallist(itens, separator, conjunction=None):
    len_itens = len(itens)
    if len_itens == 0:
        return ''
    elif len_itens == 1:
        return itens[0]
    else:
        phrase = itens[0]
        if conjunction:
            for n in range(1, len_itens - 1):
                phrase += separator + SPACE + itens[n]
            phrase += SPACE + conjunction + SPACE + itens[len_itens - 1]
        else:
            for n in range(1, len_itens):
                phrase += separator + SPACE + itens[n]
        return phrase
