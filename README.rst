Humanizer Portugues
===================

**SUPERSEEDED BY: https://github.com/staticdev/human-readable.**

|PyPI| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/humanizer-portugues.svg
   :target: https://pypi.org/project/humanizer-portugues/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/humanizer-portugues
   :target: https://pypi.org/project/humanizer-portugues
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/humanizer-portugues
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/humanizer-portugues/latest.svg?label=Read%20the%20Docs
   :target: https://humanizer-portugues.readthedocs.io/
   :alt: Read the documentation at https://humanizer-portugues.readthedocs.io/
.. |Tests| image:: https://github.com/staticdev/humanizer-portugues/workflows/Tests/badge.svg
   :target: https://github.com/staticdev/humanizer-portugues/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/staticdev/humanizer-portugues/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/staticdev/humanizer-portugues
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

* This lib contains various humanization methods such as transforming a time difference in a human-readable duration "três minutos atrás" (three minutes ago) or in a phrase.


Requirements
------------

* It works in Python 3.7 and 3.8.


Installation
------------

You can install *Humanizer Portugues* via pip_ from PyPI_:

.. code:: console

   $ pip install humanizer-portugues


Usage
-----

Import the lib with:

.. code-block:: python

   import humanizer_portugues


Humanization filesizes:

.. code-block:: python

   humanizer_portugues.natural_size(1000000)
   "1.0 MB"

   humanizer_portugues.natural_size(1000000, binary=True)
   "976.6 KiB"

   humanizer_portugues.natural_size(1000000, gnu=True)
   "976.6K"


Humanization of lists:

.. code-block:: python

   humanizer_portugues.natural_list(["Cláudio", "Maria"], ",")
   "Cláudio, Maria"

   humanizer_portugues.natural_list(["Cláudio", "Maria"], ",", "e")
   "Cláudio e Maria"

   humanizer_portugues.natural_list(["Cláudio", "Maria", "José"], ";", "ou")
   "Cláudio; Maria ou José"


Humanization of integers:

.. code-block:: python

   humanizer_portugues.ap_number(4)
   "quatro"

   humanizer_portugues.ap_number(41)
   "41"

   humanizer_portugues.int_comma(12345)
   "12,345"

   humanizer_portugues.int_word(123455913)
   "123.5 milhão"

   humanizer_portugues.int_word(12345591313)
   "12.3 bilhão"


Humanization of floating point numbers:

.. code-block:: python

   humanizer_portugues.fractional(1/3)
   "1/3"

   humanizer_portugues.fractional(1.5)
   "1 1/2"

   humanizer_portugues.fractional(0.3)
   "3/10"

   humanizer_portugues.fractional(0.333)
   "333/1000"

   humanizer_portugues.fractional(1)
   "1"


Humanization of dates and time:

.. code-block:: python

   import datetime

   humanizer_portugues.natural_clock(datetime.time(0, 30, 0))
   "zero hora e trinta minutos"

   humanizer_portugues.natural_clock(datetime.time(0, 30, 0), formal=False)
   "meia noite e meia"

   humanizer_portugues.natural_date(datetime.date(2007, 6, 5))
   "5 de junho de 2007"

   humanizer_portugues.natural_day(datetime.datetime.now())
   "hoje"

   humanizer_portugues.natural_day(datetime.datetime.now() - datetime.timedelta(days=1))
   "ontem"

   humanizer_portugues.natural_day(datetime.date(2007, 6, 5))
   "5 de junho"

   humanizer_portugues.natural_delta(datetime.timedelta(seconds=1001))
   "16 minutos"

   humanizer_portugues.natural_period(datetime.time(5, 30, 0).hour)
   "manhã"

   humanizer_portugues.natural_time(datetime.datetime.now() - datetime.timedelta(seconds=1))
   "há um segundo"

   humanizer_portugues.natural_time(datetime.datetime.now() - datetime.timedelta(seconds=3600))
   "há uma hora"


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the MIT_ license,
*Humanizer Portugues* is free and open source software.


Credits
-------

This lib is based on original humanize_, with updates for python3, translation fixes for portuguese, changes in return format and the addition of list humanizing. Localization (i18n) was also removed.


.. _MIT: http://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _pip: https://pip.pypa.io/
.. _humanize: https://github.com/jmoiron/humanize
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
