#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests base classes."""
from typing import Callable
from typing import List
from typing import Tuple
from typing import Union
from unittest import TestCase


class HumanizeTestCase(TestCase):
    """Parent test case class for this package."""

    def assertManyResults(
        self, function: Callable, args: Union[List, Tuple], results: Union[List, Tuple]
    ):
        """Utility method for multiple assertions.

        Goes through a list of arguments and makes sure that function called
        upon them lists a similarly ordered list of results.  If more than one
        argument is required, each position in args may be a tuple.

        Args:
            function (Callable): method.
            args (Union[List, Tuple]): list or tuple of arguments.
            results (Union[List, Tuple]): list or tuple of results.
        """
        for arg, result in zip(args, results):
            if isinstance(arg, tuple):
                self.assertEqual(function(*arg), result)
            else:
                self.assertEqual(function(arg), result)

    def assertEqualDatetime(self, dt1, dt2):
        """Utility method for comparing datetimes."""
        self.assertEqual((dt1 - dt2).seconds, 0)

    def assertEqualTimedelta(self, td1, td2):
        """Utility method for comparing timedeltas."""
        self.assertEqual(td1.days, td2.days)
        self.assertEqual(td1.seconds, td2.seconds)
