#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bits & Bytes related humanization."""


def natural_size(
    value: int, binary: bool = False, gnu: bool = False, formatting: str = "%.1f"
) -> str:
    """Returns human-readable file size.

    Format a number of byteslike a human readable filesize (eg. 10 kB).  By
    default, decimal suffixes (kB, MB) are used.  Passing binary=true will use
    binary suffixes (KiB, MiB) are used and the base will be 2**10 instead of
    10**3.  If ``gnu`` is True, the binary argument is ignored and GNU-style
    (ls -sh style) prefixes are used (K, M) with the 2**10 definition.
    Non-gnu modes are compatible with jinja2's ``filesizeformat`` filter.

    Args:
        value (int): size number.
        binary (bool): binary format. Defaults to False.
        gnu (bool): GNU format. Defaults to False.
        formatting (str): format pattern. Defaults to "%.1f".

    Returns:
        str: file size in natural language.
    """
    if gnu:
        sufs = ("K", "M", "G", "T", "P", "E", "Z", "Y")
    elif binary:
        sufs = (" KiB", " MiB", " GiB", " TiB", " PiB", " EiB", " ZiB", " YiB")
    else:
        sufs = (" kB", " MB", " GB", " TB", " PB", " EB", " ZB", " YB")

    base = 1024 if (gnu or binary) else 1000
    byte_size = float(value)

    if byte_size == 1 and not gnu:
        return "1 Byte"
    if byte_size < base and not gnu:
        return "%d Bytes" % byte_size
    if byte_size < base and gnu:
        return "%dB" % byte_size

    suf = ""
    for i, suf in enumerate(sufs):
        unit = base ** (i + 2)
        if byte_size < unit:
            return (formatting + "%s") % ((base * byte_size / unit), suf)
    return (formatting + "%s") % ((base * byte_size / unit), suf)
