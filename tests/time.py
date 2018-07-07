#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for time humanizing."""

from unittest.mock import patch

from humanizer_portugues.time import date_and_delta, naturalclock, naturaldate, naturalday, naturaldelta, naturaltime, naturalyear
from datetime import date, datetime, time, timedelta
from .base import HumanizeTestCase

today = date.today()
one_day = timedelta(days=1)
one_year = timedelta(days=365)

class fakedate(object):
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day

class faketime(object):
    def __init__(self, hour, minute, second):
        self.hour, self.minute, self.second = hour, minute, second

class TimeUtilitiesTestCase(HumanizeTestCase):
    """These are not considered "public" interfaces, but require tests anyway."""
    def test_date_and_delta(self):
        now = datetime.now()
        td = timedelta
        int_tests = (3, 29, 86399, 86400, 86401*30)
        date_tests = [now - td(seconds=x) for x in int_tests]
        td_tests = [td(seconds=x) for x in int_tests]
        results = [(now - td(seconds=x), td(seconds=x)) for x in int_tests]
        for t in (int_tests, date_tests, td_tests):
            for arg, result in zip(t, results):
                dt, d = date_and_delta(arg)
                self.assertEqualDatetime(dt, result[0])
                self.assertEqualTimedelta(d, result[1])
        self.assertEqual(date_and_delta("NaN"), (None, "NaN"))

class TimeTestCase(HumanizeTestCase):
    """Tests for the public interface of humanize.time"""
    def test_naturalclock_formal(self):
        meia_noite_meia = time(0, 30, 0)
        treze_um = time(13, 1, 0)
        dez_p_cinco = time(4, 50, 10)
        cinco_p_meiodia = time(11, 55, 0)
        vinteuma = time(21, 0, 40)
        overflowtest = faketime(120390192341, 2, 2)
        test_list = ('Not a time at all.', meia_noite_meia, treze_um, dez_p_cinco, cinco_p_meiodia, vinteuma, overflowtest)
        result_list = ('Not a time at all.', 'zero hora e trinta minutos', 'treze horas e um minuto', 'dez minutos para cinco horas', 'cinco minutos para doze horas', 'vinte e uma horas', overflowtest)
        self.assertManyResults(naturalclock, test_list, result_list)

    def test_naturalclock_informal(self):
        meia_noite_meia = time(0, 30, 0)
        treze_um = time(13, 1, 0)
        dez_p_cinco = time(4, 50, 10)
        cinco_p_meiodia = time(11, 55, 0)
        vinteuma = time(21, 0, 40)
        overflowtest = faketime(120390192341, 2, 2)
        test_list = ('Not a time at all.', meia_noite_meia, treze_um, dez_p_cinco, cinco_p_meiodia, vinteuma, overflowtest)
        result_list = ('Not a time at all.', 'meia noite e meia', 'uma e um da tarde', 'dez para cinco da manhã', 'cinco para meio dia', 'nove da noite', overflowtest)
        nc_informal = lambda d: naturalclock(d, formal=False)
        self.assertManyResults(nc_informal, test_list, result_list)

    def test_naturaldelta_nomeses(self):
        now = datetime.now()
        test_list = [
            timedelta(days=7),
            timedelta(days=31),
            timedelta(days=230),
            timedelta(days=400),
        ]
        result_list = [
            '7 dias',
            '31 dias',
            '230 dias',
            '1 ano e 35 dias',
        ]
        with patch('humanizer_portugues.time._now') as mocked:
            mocked.return_value = now
            nd_nomeses = lambda d: naturaldelta(d, months=False)
            self.assertManyResults(nd_nomeses, test_list, result_list)

    def test_naturaldelta(self):
        now = datetime.now()
        test_list = [
            0,
            1,
            30,
            timedelta(minutes=1, seconds=30),
            timedelta(minutes=2),
            timedelta(hours=1, minutes=30, seconds=30),
            timedelta(hours=23, minutes=50, seconds=50),
            timedelta(days=1),
            timedelta(days=500),
            timedelta(days=365*2 + 35),
            timedelta(seconds=1),
            timedelta(seconds=30),
            timedelta(minutes=1, seconds=30),
            timedelta(minutes=2),
            timedelta(hours=1, minutes=30, seconds=30),
            timedelta(hours=23, minutes=50, seconds=50),
            timedelta(days=1),
            timedelta(days=500),
            timedelta(days=365*2 + 35),
            # regression tests for bugs in post-release humanize
            timedelta(days=10000),
            timedelta(days=365+35),
            30,
            timedelta(days=365*2 + 65),
            timedelta(days=365 + 4),
            timedelta(days=35),
            timedelta(days=65),
            timedelta(days=9),
            timedelta(days=365),
            "NaN",
        ]
        result_list = [
            'um momento',
            'um segundo',
            '30 segundos',
            'um minuto',
            '2 minutos',
            'uma hora',
            '23 horas',
            'um dia',
            '1 ano e 4 meses',
            '2 anos',
            'um segundo',
            '30 segundos',
            'um minuto',
            '2 minutos',
            'uma hora',
            '23 horas',
            'um dia',
            '1 ano e 4 meses',
            '2 anos',
            '27 anos',
            '1 ano e 1 mês',
            '30 segundos',
            '2 anos',
            '1 ano e 4 dias',
            'um mês',
            '2 meses',
            '9 dias',
            'um ano',
            "NaN",
        ]
        with patch('humanizer_portugues.time._now') as mocked:
            mocked.return_value = now
            self.assertManyResults(naturaldelta, test_list, result_list)

    def test_naturaltime(self):
        now = datetime.now()
        test_list = [
            now,
            now - timedelta(seconds=1),
            now - timedelta(seconds=30),
            now - timedelta(minutes=1, seconds=30),
            now - timedelta(minutes=2),
            now - timedelta(hours=1, minutes=30, seconds=30),
            now - timedelta(hours=23, minutes=50, seconds=50),
            now - timedelta(days=1),
            now - timedelta(days=500),
            now - timedelta(days=365*2 + 35),
            now + timedelta(seconds=1),
            now + timedelta(seconds=30),
            now + timedelta(minutes=1, seconds=30),
            now + timedelta(minutes=2),
            now + timedelta(hours=1, minutes=30, seconds=30),
            now + timedelta(hours=23, minutes=50, seconds=50),
            now + timedelta(days=1),
            now + timedelta(days=500),
            now + timedelta(days=365*2 + 35),
            # regression tests for bugs in post-release humanize
            now + timedelta(days=10000),
            now - timedelta(days=365+35),
            30,
            now - timedelta(days=365*2 + 65),
            now - timedelta(days=365 + 4),
            "NaN",
        ]
        result_list = [
            'agora',
            'há um segundo',
            'há 30 segundos',
            'há um minuto',
            'há 2 minutos',
            'há uma hora',
            'há 23 horas',
            'há um dia',
            'há 1 ano e 4 meses',
            'há 2 anos',
            'em um segundo',
            'em 30 segundos',
            'em um minuto',
            'em 2 minutos',
            'em uma hora',
            'em 23 horas',
            'em um dia',
            'em 1 ano e 4 meses',
            'em 2 anos',
            'em 27 anos',
            'há 1 ano e 1 mês',
            'há 30 segundos',
            'há 2 anos',
            'há 1 ano e 4 dias',
            "NaN",
        ]
        with patch('humanizer_portugues.time._now') as mocked:
            mocked.return_value = now
            self.assertManyResults(naturaltime, test_list, result_list)

    def test_naturaltime_nomonths(self):
        now = datetime.now()
        test_list = [
            now,
            now - timedelta(seconds=1),
            now - timedelta(seconds=30),
            now - timedelta(minutes=1, seconds=30),
            now - timedelta(minutes=2),
            now - timedelta(hours=1, minutes=30, seconds=30),
            now - timedelta(hours=23, minutes=50, seconds=50),
            now - timedelta(days=1),
            now - timedelta(days=17),
            now - timedelta(days=47),
            now - timedelta(days=500),
            now - timedelta(days=365*2 + 35),
            now + timedelta(seconds=1),
            now + timedelta(seconds=30),
            now + timedelta(minutes=1, seconds=30),
            now + timedelta(minutes=2),
            now + timedelta(hours=1, minutes=30, seconds=30),
            now + timedelta(hours=23, minutes=50, seconds=50),
            now + timedelta(days=1),
            now + timedelta(days=500),
            now + timedelta(days=365*2 + 35),
            # regression tests for bugs in post-release humanize
            now + timedelta(days=10000),
            now - timedelta(days=365+35),
            30,
            now - timedelta(days=365*2 + 65),
            now - timedelta(days=365 + 4),
            "NaN",
        ]
        result_list = [
            'agora',
            'há um segundo',
            'há 30 segundos',
            'há um minuto',
            'há 2 minutos',
            'há uma hora',
            'há 23 horas',
            'há um dia',
            'há 17 dias',
            'há 47 dias',
            'há 1 ano e 135 dias',
            'há 2 anos',
            'em um segundo',
            'em 30 segundos',
            'em um minuto',
            'em 2 minutos',
            'em uma hora',
            'em 23 horas',
            'em um dia',
            'em 1 ano e 135 dias',
            'em 2 anos',
            'em 27 anos',
            'há 1 ano e 35 dias',
            'há 30 segundos',
            'há 2 anos',
            'há 1 ano e 4 dias',
            "NaN",
        ]
        with patch('humanizer_portugues.time._now') as mocked:
            mocked.return_value = now
            nt_nomonths = lambda d: naturaltime(d, months=False)
            self.assertManyResults(nt_nomonths, test_list, result_list)

    def test_naturalday(self):
        tomorrow = today + one_day
        yesterday = today - one_day
        if today.month != 3:
            someday = date(today.year, 3, 5)
            someday_result = 'em 05 de março'
        else:
            someday = date(today.year, 9, 5)
            someday_result = 'em 05 de setembro'
        valerrtest = fakedate(290149024, 2, 2)
        overflowtest = fakedate(120390192341, 2, 2)
        test_list = (today, tomorrow, yesterday, someday, '02/26/1984',
            None, "Not a date at all.", valerrtest, overflowtest
        )
        result_list = ('hoje', 'amanhã', 'ontem', someday_result, '02/26/1984',
            None, "Not a date at all.", valerrtest, overflowtest
        )
        self.assertManyResults(naturalday, test_list, result_list)

    def test_naturaldate(self):
        tomorrow = today + one_day
        yesterday = today - one_day

        if today.month != 3:
            someday = date(today.year, 3, 5)
            someday_result = 'em 05 de março'
        else:
            someday = date(today.year, 9, 5)
            someday_result = 'em 05 de setembro'
        valerrtest = fakedate(290149024, 2, 2)
        overflowtest = fakedate(120390192341, 2, 2)

        test_list = (today, tomorrow, yesterday, someday, date(1982, 6, 27), 
            None, "Not a date at all.", valerrtest, overflowtest
        )
        result_list = ('hoje', 'amanhã', 'ontem', someday_result, 'em 27 de junho de 1982',
            None, "Not a date at all.", valerrtest, overflowtest
        )
        self.assertManyResults(naturaldate, test_list, result_list)

    def test_naturalyear(self):
        next_year = today + one_year
        last_year = today - one_year

        someyear = fakedate(1988, 1, 1)
        valerrtest = fakedate(290149024, 2, 2)
        overflowtest = fakedate(120390192341, 2, 2)
        test_list = (today, next_year, last_year, '1955', someyear,
            None, "Not a date at all.", valerrtest, overflowtest
        )
        result_list = ('este ano', 'ano que vem', 'ano passado', '1955', '1988',
            None, "Not a date at all.", valerrtest, overflowtest
        )
        self.assertManyResults(naturalyear, test_list, result_list)
