#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests base classes."""
import datetime
from typing import Any
from typing import Callable
from typing import List
from unittest import TestCase


class HumanizeTestCase(TestCase):
    """Parent test case class for this package."""

    def assert_many_results(
        self, function: Callable[..., Any], args: List[Any], results: List[Any],
    ) -> None:
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

    def assert_equal_datetime(
        self, dt1: datetime.datetime, dt2: datetime.datetime
    ) -> None:
        """Utility method for comparing datetimes."""
        self.assertEqual((dt1 - dt2).seconds, 0)

    def assert_equal_timedelta(
        self, td1: datetime.timedelta, td2: datetime.timedelta
    ) -> None:
        """Utility method for comparing timedeltas."""
        self.assertEqual(td1.days, td2.days)
        self.assertEqual(td1.seconds, td2.seconds)
