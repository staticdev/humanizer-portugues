#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Number tests."""
import humanizer_portugues.number
from .base import HumanizeTestCase


class NumberTestCase(HumanizeTestCase):
    """Test case class for numbers."""

    def test_ordinal(self) -> None:
        """Tests ordinal method."""
        test_list = [
            "1",
            "2",
            "3",
            "4",
            "11",
            "12",
            "13",
            "101",
            "102",
            "103",
            "111",
            "something else",
            None,
        ]
        result_list = [
            "1º",
            "2º",
            "3º",
            "4º",
            "11º",
            "12º",
            "13º",
            "101º",
            "102º",
            "103º",
            "111º",
            "something else",
            None,
        ]
        self.assert_many_results(
            humanizer_portugues.number.ordinal, test_list, result_list
        )

    def test_int_comma(self) -> None:
        """Tests int_comma method."""
        test_list = [
            100,
            1000,
            10123,
            10311,
            1000000,
            1234567.25,
            "100",
            "1000",
            "10123",
            "10311",
            "1000000",
            "1234567.1234567",
            None,
        ]
        result_list = [
            "100",
            "1,000",
            "10,123",
            "10,311",
            "1,000,000",
            "1,234,567.25",
            "100",
            "1,000",
            "10,123",
            "10,311",
            "1,000,000",
            "1,234,567.1234567",
            None,
        ]
        self.assert_many_results(
            humanizer_portugues.number.int_comma, test_list, result_list
        )

    def test_int_word(self) -> None:
        """Tests int_word method."""
        # make sure that POWERS & HUMAN_POWERS have the same number of items
        self.assertEqual(
            len(humanizer_portugues.number.POWERS),
            len(humanizer_portugues.number.HUMAN_POWERS),
        )
        # test the result of int_word
        test_list = [
            "100",
            "1000000",
            "1200000",
            "1290000",
            "1000000000",
            "2000000000",
            "6000000000000",
            "1300000000000000",
            "3500000000000000000000",
            "8100000000000000000000000000000000",
            None,
            ("1230000", "%0.2f"),
            10 ** 101,
        ]
        result_list = [
            "100",
            "1.0 milhão",
            "1.2 milhão",
            "1.3 milhão",
            "1.0 bilhão",
            "2.0 bilhão",
            "6.0 trilhão",
            "1.3 quatrilhão",
            "3.5 sextilhão",
            "8.1 decilhão",
            None,
            "1.23 milhão",
            "1" + "0" * 101,
        ]
        self.assert_many_results(
            humanizer_portugues.number.int_word, test_list, result_list
        )

    def test_ap_number(self) -> None:
        """Tests ap_number method."""
        test_list = [1, 2, 4, 5, 9, 10, "7", None]
        result_list = ["um", "dois", "quatro", "cinco", "nove", "10", "sete", None]
        self.assert_many_results(
            humanizer_portugues.number.ap_number, test_list, result_list
        )

    def test_fractional(self) -> None:
        """Tests fractional method."""
        test_list = [1, 2.0, (4.0 / 3.0), (5.0 / 6.0), "7", "8.9", "dez", None]
        result_list = ["1", "2", "1 1/3", "5/6", "7", "8 9/10", "dez", None]
        self.assert_many_results(
            humanizer_portugues.number.fractional, test_list, result_list
        )
