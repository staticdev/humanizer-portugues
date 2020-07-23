"""__init__ tests."""
import datetime

import humanizer_portugues


def test_natural_size() -> None:
    """Call of natural_size from humanizer_portugues."""
    assert humanizer_portugues.natural_size(1000000) == "1.0 MB"


def test_natural_list() -> None:
    """Call of natural_list from humanizer_portugues."""
    assert (
        humanizer_portugues.natural_list(["Cláudio", "Maria"], ",") == "Cláudio, Maria"
    )


def test_ap_number() -> None:
    """Call of ap_number from humanizer_portugues."""
    assert humanizer_portugues.ap_number(4) == "quatro"


def test_int_comma() -> None:
    """Call of int_comma from humanizer_portugues."""
    assert humanizer_portugues.int_comma(12345) == "12,345"


def test_int_word() -> None:
    """Call of int_word from humanizer_portugues."""
    assert humanizer_portugues.int_word(123455913) == "123.5 milhão"


def test_fractional() -> None:
    """Call of fractional from humanizer_portugues."""
    assert humanizer_portugues.fractional(1 / 3) == "1/3"


def test_natural_clock() -> None:
    """Call of natural_clock from humanizer_portugues."""
    date = datetime.time(0, 30, 0)
    assert humanizer_portugues.natural_clock(date) == "zero hora e trinta minutos"


def test_natural_date() -> None:
    """Call of natural_date from humanizer_portugues."""
    date = datetime.date(2007, 6, 5)
    assert humanizer_portugues.natural_date(date) == "5 de junho de 2007"


def test_natural_day() -> None:
    """Call of natural_day from humanizer_portugues."""
    assert humanizer_portugues.natural_day(datetime.datetime.now()) == "hoje"


def test_natural_delta() -> None:
    """Call of natural_delta from humanizer_portugues."""
    delta = datetime.timedelta(seconds=1001)
    assert humanizer_portugues.natural_delta(delta) == "16 minutos"


def test_natural_period() -> None:
    """Call of natural_period from humanizer_portugues."""
    assert humanizer_portugues.natural_period(datetime.time(5, 30, 0).hour) == "manhã"


def test_natural_time() -> None:
    """Call of natural_time from humanizer_portugues."""
    assert (
        humanizer_portugues.natural_time(
            datetime.datetime.now() - datetime.timedelta(seconds=1)
        )
        == "há um segundo"
    )
