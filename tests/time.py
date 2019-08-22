#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for time humanizing."""

import datetime
import unittest.mock

import humanizer_portugues.time
from .base import HumanizeTestCase

TODAY = datetime.date.today()
ONE_DAY = datetime.timedelta(days=1)
ONE_YEAR = datetime.timedelta(days=365)


class FakeDate():
    """Test helper to fake date"""
    def __init__(self, year, month, day):
        self.year, self.month, self.day = year, month, day


class FakeTime():
    """Test helper class to fake time"""
    def __init__(self, hour, minute, second):
        self.hour, self.minute, self.second = hour, minute, second


class TimeUtilitiesTestCase(HumanizeTestCase):
    """These are not considered "public" interfaces, but require tests anyway.
    """
    def test_date_and_delta(self):
        """Tests date_and_delta utility method"""
        now = datetime.datetime.now()
        tdelta = datetime.timedelta
        int_tests = (3, 29, 86399, 86400, 86401*30)
        date_tests = [now - tdelta(seconds=x) for x in int_tests]
        td_tests = [tdelta(seconds=x) for x in int_tests]
        results = [(now - tdelta(seconds=x),
                    tdelta(seconds=x)) for x in int_tests]
        for test in (int_tests, date_tests, td_tests):
            for arg, result in zip(test, results):
                dtime, delta = humanizer_portugues.time.date_and_delta(arg)
                self.assertEqualDatetime(dtime, result[0])
                self.assertEqualTimedelta(delta, result[1])
        self.assertEqual(humanizer_portugues.time.date_and_delta("NaN"),
                         (None, "NaN"))


class TimeTestCase(HumanizeTestCase):
    """Tests for the public interface of humanize.time"""
    def test_naturalclock_formal(self):
        """Tests naturalclock method"""
        meia_noite_meia = datetime.time(0, 30, 0)
        treze_um = datetime.time(13, 1, 0)
        dez_p_cinco = datetime.time(4, 50, 10)
        cinco_p_meiodia = datetime.time(11, 55, 0)
        vinteuma = datetime.time(21, 0, 40)
        overflowtest = FakeTime(120390192341, 2, 2)
        test_list = ('Not a time at all.', meia_noite_meia, treze_um,
                     dez_p_cinco, cinco_p_meiodia, vinteuma, overflowtest)
        result_list = ('Not a time at all.', 'zero hora e trinta minutos',
                       'treze horas e um minuto',
                       'dez minutos para cinco horas',
                       'cinco minutos para doze horas', 'vinte e uma horas',
                       overflowtest)
        self.assertManyResults(humanizer_portugues.time.naturalclock,
                               test_list, result_list)

    def test_naturalclock_informal(self):
        """Tests naturalclock method with formal=False"""
        meia_noite_meia = datetime.time(0, 30, 0)
        treze_um = datetime.time(13, 1, 0)
        dez_p_cinco = datetime.time(4, 50, 10)
        cinco_p_meiodia = datetime.time(11, 55, 0)
        vinteuma = datetime.time(21, 0, 40)
        overflowtest = FakeTime(120390192341, 2, 2)
        test_list = ('Not a time at all.', meia_noite_meia, treze_um,
                     dez_p_cinco, cinco_p_meiodia, vinteuma, overflowtest)
        result_list = ('Not a time at all.', 'meia noite e meia',
                       'uma e um da tarde', 'dez para cinco da manhã',
                       'cinco para meio dia', 'nove da noite', overflowtest)
        self.assertManyResults(
            lambda d: humanizer_portugues.time.naturalclock(d, formal=False),
            test_list, result_list)

    @unittest.mock.patch('humanizer_portugues.time._now')
    def test_naturaldelta_nomonths(self, mocked):
        """Tests naturaldelta method with months=False"""
        now = datetime.datetime.now()
        mocked.return_value = now
        test_list = [
            datetime.timedelta(days=7),
            datetime.timedelta(days=31),
            datetime.timedelta(days=230),
            datetime.timedelta(days=366),
            datetime.timedelta(days=400),
        ]
        result_list = [
            '7 dias',
            '31 dias',
            '230 dias',
            '1 ano e 1 dia',
            '1 ano e 35 dias',
        ]
        self.assertManyResults(
            lambda d: humanizer_portugues.time.naturaldelta(d, months=False),
            test_list, result_list)

    @unittest.mock.patch('humanizer_portugues.time._now')
    def test_naturaldelta(self, mocked):
        """Tests naturaldelta method"""
        now = datetime.datetime.now()
        mocked.return_value = now
        test_list = [
            0,
            1,
            30,
            datetime.timedelta(minutes=1, seconds=30),
            datetime.timedelta(minutes=2),
            datetime.timedelta(hours=1, minutes=30, seconds=30),
            datetime.timedelta(hours=23, minutes=50, seconds=50),
            datetime.timedelta(days=1),
            datetime.timedelta(days=500),
            datetime.timedelta(days=365*2 + 35),
            datetime.timedelta(seconds=1),
            datetime.timedelta(seconds=30),
            datetime.timedelta(minutes=1, seconds=30),
            datetime.timedelta(minutes=2),
            datetime.timedelta(hours=1, minutes=30, seconds=30),
            datetime.timedelta(hours=23, minutes=50, seconds=50),
            datetime.timedelta(days=1),
            datetime.timedelta(days=500),
            datetime.timedelta(days=365*2 + 35),
            # regression tests for bugs in post-release humanize
            datetime.timedelta(days=10000),
            datetime.timedelta(days=365+35),
            30,
            datetime.timedelta(days=365*2 + 65),
            datetime.timedelta(days=365 + 1),
            datetime.timedelta(days=365 + 4),
            datetime.timedelta(days=35),
            datetime.timedelta(days=65),
            datetime.timedelta(days=9),
            datetime.timedelta(days=365),
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
            '1 ano e 1 dia',
            '1 ano e 4 dias',
            'um mês',
            '2 meses',
            '9 dias',
            'um ano',
            "NaN",
        ]
        self.assertManyResults(humanizer_portugues.time.naturaldelta,
                               test_list, result_list)

    @unittest.mock.patch('humanizer_portugues.time._now')
    def test_naturaltime(self, mocked):
        """Tests naturaltime method"""
        now = datetime.datetime.now()
        mocked.return_value = now
        test_list = [
            now,
            now - datetime.timedelta(seconds=1),
            now - datetime.timedelta(seconds=30),
            now - datetime.timedelta(minutes=1, seconds=30),
            now - datetime.timedelta(minutes=2),
            now - datetime.timedelta(hours=1, minutes=30, seconds=30),
            now - datetime.timedelta(hours=23, minutes=50, seconds=50),
            now - datetime.timedelta(days=1),
            now - datetime.timedelta(days=500),
            now - datetime.timedelta(days=365*2 + 35),
            now + datetime.timedelta(seconds=1),
            now + datetime.timedelta(seconds=30),
            now + datetime.timedelta(minutes=1, seconds=30),
            now + datetime.timedelta(minutes=2),
            now + datetime.timedelta(hours=1, minutes=30, seconds=30),
            now + datetime.timedelta(hours=23, minutes=50, seconds=50),
            now + datetime.timedelta(days=1),
            now + datetime.timedelta(days=500),
            now + datetime.timedelta(days=365*2 + 35),
            # regression tests for bugs in post-release humanize
            now + datetime.timedelta(days=10000),
            now - datetime.timedelta(days=365+35),
            30,
            now - datetime.timedelta(days=365*2 + 65),
            now - datetime.timedelta(days=365 + 4),
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
        self.assertManyResults(humanizer_portugues.time.naturaltime,
                               test_list, result_list)

    @unittest.mock.patch('humanizer_portugues.time._now')
    def test_naturaltime_nomonths(self, mocked):
        """Tests naturaltime method with months=False"""
        now = datetime.datetime.now()
        mocked.return_value = now
        test_list = [
            now,
            now - datetime.timedelta(seconds=1),
            now - datetime.timedelta(seconds=30),
            now - datetime.timedelta(minutes=1, seconds=30),
            now - datetime.timedelta(minutes=2),
            now - datetime.timedelta(hours=1, minutes=30, seconds=30),
            now - datetime.timedelta(hours=23, minutes=50, seconds=50),
            now - datetime.timedelta(days=1),
            now - datetime.timedelta(days=17),
            now - datetime.timedelta(days=47),
            now - datetime.timedelta(days=500),
            now - datetime.timedelta(days=365*2 + 35),
            now + datetime.timedelta(seconds=1),
            now + datetime.timedelta(seconds=30),
            now + datetime.timedelta(minutes=1, seconds=30),
            now + datetime.timedelta(minutes=2),
            now + datetime.timedelta(hours=1, minutes=30, seconds=30),
            now + datetime.timedelta(hours=23, minutes=50, seconds=50),
            now + datetime.timedelta(days=1),
            now + datetime.timedelta(days=500),
            now + datetime.timedelta(days=365*2 + 35),
            # regression tests for bugs in post-release humanize
            now + datetime.timedelta(days=10000),
            now - datetime.timedelta(days=365+35),
            30,
            now - datetime.timedelta(days=365*2 + 65),
            now - datetime.timedelta(days=365 + 4),
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
        self.assertManyResults(
            lambda d: humanizer_portugues.time.naturaltime(d, months=False),
            test_list, result_list)

    def test_naturalday(self):
        """Tests naturalday method"""
        tomorrow = TODAY + ONE_DAY
        yesterday = TODAY - ONE_DAY
        if TODAY.month != 3:
            someday = datetime.date(TODAY.year, 3, 5)
            someday_result = '5 de março'
        else:
            someday = datetime.date(TODAY.year, 9, 5)
            someday_result = '5 de setembro'
        valerrtest = FakeDate(290149024, 2, 2)
        overflowtest = FakeDate(120390192341, 2, 2)
        test_list = (TODAY, tomorrow, yesterday, someday, '02/26/1984',
                     None, "Not a date at all.", valerrtest, overflowtest)
        result_list = ('hoje', 'amanhã', 'ontem', someday_result, '02/26/1984',
                       None, "Not a date at all.", valerrtest, overflowtest)
        self.assertManyResults(humanizer_portugues.time.naturalday,
                               test_list, result_list)

    def test_naturaldate(self):
        """Tests naturaldate method"""
        tomorrow = TODAY + ONE_DAY
        yesterday = TODAY - ONE_DAY

        if TODAY.month != 3:
            someday = datetime.date(TODAY.year, 3, 5)
            someday_result = '5 de março'
        else:
            someday = datetime.date(TODAY.year, 9, 5)
            someday_result = '5 de setembro'
        valerrtest = FakeDate(290149024, 2, 2)
        overflowtest = FakeDate(120390192341, 2, 2)

        test_list = (TODAY, tomorrow, yesterday, someday,
                     datetime.date(1982, 6, 27), None, "Not a date at all.",
                     valerrtest, overflowtest)
        result_list = ('hoje', 'amanhã', 'ontem', someday_result,
                       '27 de junho de 1982', None, "Not a date at all.",
                       valerrtest, overflowtest)
        self.assertManyResults(humanizer_portugues.time.naturaldate,
                               test_list, result_list)

    def test_naturalyear(self):
        """Tests naturalyear method"""
        next_year = TODAY + ONE_YEAR
        last_year = TODAY - ONE_YEAR

        someyear = FakeDate(1988, 1, 1)
        valerrtest = FakeDate(290149024, 2, 2)
        overflowtest = FakeDate(120390192341, 2, 2)
        test_list = (TODAY, next_year, last_year, '1955', someyear,
                     None, "Not a date at all.", valerrtest, overflowtest)
        result_list = ('este ano', 'ano que vem', 'ano passado', '1955',
                       '1988', None, "Not a date at all.", valerrtest,
                       overflowtest)
        self.assertManyResults(humanizer_portugues.time.naturalyear,
                               test_list, result_list)
