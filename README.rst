humanizer-portugues
===================

.. image:: https://secure.travis-ci.org/staticdev/humanizer-portugues.png?branch=master
  :target: http://travis-ci.org/staticdev/humanizer-portugues

Este pacote contém várias funções de humanização (humanization), como transformar um número em uma duração legível para humanos ('três minutos atrás') ou em uma frase. Ele funciona em python2 e 3, sendo recomendado o uso da versão mais recente.

Este código é baseado no pacote original humanize, com correções de tradução, formato e adição de humanização de listas. Além disso, foi retirado o recurso de localização (i18n) facilitando sua utilização para português.

Uso
---

Para importar o pacote basta executar:

.. code-block:: python

    import humanize

Humanization de inteiros:

.. code-block:: python

    humanize.intcomma(12345)
    '12,345'
    
    humanize.intword(123455913)
    '123.5 million'
    
    humanize.intword(12345591313)
    '12.3 billion'
    
    humanize.apnumber(4)
    'four'
    
    humanize.apnumber(41)
    '41'

Humanization datas e horas:

.. code-block:: python

    import datetime
    humanize.naturalday(datetime.datetime.now())
    'today'
    
    humanize.naturaldelta(datetime.timedelta(seconds=1001))
    '16 minutes'
    
    humanize.naturalday(datetime.datetime.now() - datetime.timedelta(days=1))
    'yesterday'
    
    humanize.naturalday(datetime.date(2007, 6, 5))
    'Jun 05'
    
    humanize.naturaldate(datetime.date(2007, 6, 5))
    'Jun 05 2007'
    
    humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=1))
    'a second ago'
    
    humanize.naturaltime(datetime.datetime.now() - datetime.timedelta(seconds=3600))
    'an hour ago'

Humanization de tamanho de arquivos:

.. code-block:: python

    humanize.naturalsize(1000000)
    '1.0 MB'
    
    humanize.naturalsize(1000000, binary=True)
    '976.6 KiB'
    
    humanize.naturalsize(1000000, gnu=True)
    '976.6K'

Humanization de números de ponto flutuante:

.. code-block:: python

    humanize.fractional(1/3)
    '1/3'
    
    humanize.fractional(1.5)
    '1 1/2'
    
    humanize.fractional(0.3)
    '3/10'
    
    humanize.fractional(0.333)
    '1/3'
    
    humanize.fractional(1)
    '1'

Humanization de listas:

.. code-block:: python

    humanize.list_to_phrase(['Cláudio', 'Maria'], ',', 'e')
    'Cláudio e Maria'