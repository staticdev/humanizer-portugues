#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for filesize humanizing."""
import humanizer_portugues.list
from .base import HumanizeTestCase


class ListTestCase(HumanizeTestCase):
    """Test case class for lists."""

    def test_natural_list(self):
        """Tests natural_list method."""
        tests = (
            ([], "", ""),
            (["jorbas"], ","),
            (["Jorbas"], ",", "and"),
            (["jorbas", "maria"], ","),
            (["jorbas", "maria"], ",", "e"),
            (["jorbas", "maria", "gustavo"], ";"),
            (["jorbas", "maria", "gustavo"], ";", "ou"),
        )
        results = (
            "",
            "jorbas",
            "Jorbas",
            "jorbas, maria",
            "jorbas e maria",
            "jorbas; maria; gustavo",
            "jorbas; maria ou gustavo",
        )
        self.assertManyResults(humanizer_portugues.list.natural_list, tests, results)
