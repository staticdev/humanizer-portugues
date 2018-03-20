#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for filesize humanizing."""

from humanizer_portugues.list import naturallist
from .base import HumanizeTestCase

class ListTestCase(HumanizeTestCase):
    def test_naturallist(self):
        tests = (([], '', ''), (['jorbas'], ','), (['Jorbas'], ',', 'and'), (['jorbas', 'maria'], ','),
            (['jorbas', 'maria'], ',', 'e'), (['jorbas', 'maria', 'gustavo'], ';'), 
            (['jorbas', 'maria', 'gustavo'], ';', 'ou'))
        results = ('', 'jorbas', 'Jorbas', 'jorbas, maria',
            'jorbas e maria', 'jorbas; maria; gustavo',
            'jorbas; maria ou gustavo')
        self.assertManyResults(naturallist, tests, results)
