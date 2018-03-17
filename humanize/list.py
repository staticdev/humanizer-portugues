#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['list_to_phrase']

SPACE = ' '

def list_to_phrase(itens, separator, conjunction):
    len_itens = len(itens)
    if len(itens) == 1:
        return itens[0]
    else:
        phrase = itens[0]
        for n in range(1, len_itens - 1):
             phrase += separator + SPACE + itens[n]
        phrase += SPACE + conjunction + SPACE + itens[len_itens - 1]
        return phrase
