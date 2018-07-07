humanizer-portugues
===================

|pyversions| |Travis| |Codecov| |PyPi|

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/humanizer-portugues.svg
    :target: https://pypi.python.org/pypi/humanizer-portugues
    :alt: Python versions supported

.. |Travis| image:: https://api.travis-ci.org/staticdev/humanizer-portugues.svg?branch=master
.. _Travis: https://travis-ci.org/staticdev/humanizer-portugues

.. |Codecov| image:: https://codecov.io/github/staticdev/humanizer-portugues/badge.svg?branch=master&service=github
.. _Codecov: https://codecov.io/github/staticdev/humanizer-portugues?branch=master

.. |PyPi| image:: https://badge.fury.io/py/humanizer-portugues.svg
.. _PyPi: https://badge.fury.io/py/humanizer-portugues

Este pacote contém várias funções de humanização (humanization), como transformar um número em uma duração legível para humanos ('três minutos atrás') ou em uma frase. Ele funciona em python2 e 3, sendo recomendado o uso da versão mais recente.

Este código é baseado no pacote original humanize_, com atualização para python3, correções de tradução, formato e adição de humanização de listas. Além disso, foi retirado o recurso de localização (i18n) facilitando sua utilização para português.

Instalação
----------

Para instalar o ``humanizer-portugues`` execute o comando:

.. code-block:: sh

      pip install humanizer-portugues

Uso
---

Para importar o pacote basta executar:

.. code-block:: python

    import humanizer_portugues

Humanization de inteiros:

.. code-block:: python

    humanizer_portugues.intcomma(12345)
    '12,345'
    
    humanizer_portugues.intword(123455913)
    '123.5 milhão'
    
    humanizer_portugues.intword(12345591313)
    '12.3 bilhão'
    
    humanizer_portugues.apnumber(4)
    'quatro'
    
    humanizer_portugues.apnumber(41)
    '41'

Humanization datas e horas:

.. code-block:: python

    import datetime
    humanizer_portugues.naturalclock(datetime.time(13, 1, 0))
    'zero hora e trinta minutos'

    humanizer_portugues.naturalclock(datetime.time(13, 1, 0), formal=False)
    'meia noite e meia'

    humanizer_portugues.naturalday(datetime.datetime.now())
    'hoje'
    
    humanizer_portugues.naturaldelta(datetime.timedelta(seconds=1001))
    '16 minutos'
    
    humanizer_portugues.naturalday(datetime.datetime.now() - datetime.timedelta(days=1))
    'ontem'
    
    humanizer_portugues.naturalday(datetime.date(2007, 6, 5))
    'em 05 de junho'
    
    humanizer_portugues.naturaldate(datetime.date(2007, 6, 5))
    'em 05 de junho de 2007'
    
    humanizer_portugues.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=1))
    'há um segundo'
    
    humanizer_portugues.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=3600))
    'há uma hora'

Humanization de tamanho de arquivos:

.. code-block:: python

    humanizer_portugues.naturalsize(1000000)
    '1.0 MB'
    
    humanizer_portugues.naturalsize(1000000, binary=True)
    '976.6 KiB'
    
    humanizer_portugues.naturalsize(1000000, gnu=True)
    '976.6K'

Humanization de números de ponto flutuante:

.. code-block:: python

    humanizer_portugues.fractional(1/3)
    '1/3'
    
    humanizer_portugues.fractional(1.5)
    '1 1/2'
    
    humanizer_portugues.fractional(0.3)
    '3/10'
    
    humanizer_portugues.fractional(0.333)
    '333/1000'
    
    humanizer_portugues.fractional(1)
    '1'

Humanization de listas:

.. code-block:: python

    humanizer_portugues.naturallist(['Cláudio', 'Maria'], ',')
    'Cláudio, Maria'

    humanizer_portugues.naturallist(['Cláudio', 'Maria'], ',', 'e')
    'Cláudio e Maria'

    humanizer_portugues.naturallist(['Cláudio', 'Maria', 'José'], ';', 'ou')
    'Cláudio; Maria ou José'

.. _Humanize: https://github.com/jmoiron/humanize