"""Humanizer portugues."""
try:
    from importlib.metadata import version, PackageNotFoundError  # type: ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import version, PackageNotFoundError  # type: ignore

from humanizer_portugues.filesize import natural_size
from humanizer_portugues.list import natural_list
from humanizer_portugues.number import fractional, int_comma, int_word, ordinal
from humanizer_portugues.time import (
    natural_date,
    natural_day,
    natural_period,
    natural_time,
    natural_year,
)

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"

__all__ = [
    "ap_number",
    "fractional",
    "int_comma",
    "int_word",
    "natural_date",
    "natural_day",
    "natural_delta",
    "natural_list",
    "natural_period",
    "natural_size",
    "natural_time",
    "natural_year",
    "ordinal",
]
