#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for filesize humanizing."""
import humanizer_portugues.filesize
from .base import HumanizeTestCase


class FilesizeTestCase(HumanizeTestCase):
    """Test case class for file size."""

    def test_natural_size(self) -> None:
        """Tests natural_size method."""
        tests = [
            1,
            300,
            3000,
            3000000,
            3000000000,
            3000000000000,
            (300, True),
            (3000, True),
            (3000000, True),
            (300, False, True),
            (3000, False, True),
            (3000000, False, True),
            (1024, False, True),
            (10 ** 26 * 30, False, True),
            (10 ** 26 * 30, True),
            10 ** 26 * 30,
            (3141592, False, False, "%.2f"),
            (3000, False, True, "%.3f"),
            (3000000000, False, True, "%.0f"),
            (10 ** 26 * 30, True, False, "%.3f"),
        ]
        results = [
            "1 Byte",
            "300 Bytes",
            "3.0 kB",
            "3.0 MB",
            "3.0 GB",
            "3.0 TB",
            "300 Bytes",
            "2.9 KiB",
            "2.9 MiB",
            "300B",
            "2.9K",
            "2.9M",
            "1.0K",
            "2481.5Y",
            "2481.5 YiB",
            "3000.0 YB",
            "3.14 MB",
            "2.930K",
            "3G",
            "2481.542 YiB",
        ]
        self.assert_many_results(
            humanizer_portugues.filesize.natural_size, tests, results
        )
