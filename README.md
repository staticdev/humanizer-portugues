# humanizer-portugues

[![Tests](https://github.com/staticdev/humanizer-portugues/workflows/Tests/badge.svg)](https://github.com/staticdev/humanizer-portugues/actions?workflow=Tests)
[![Codecov](https://codecov.io/gh/staticdev/humanizer-portugues/badge.svg?branch=master&service=github)](https://codecov.io/gh/staticdev/humanizer-portugues)
![PyPi](https://badge.fury.io/py/humanizer-portugues.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Este pacote contém várias funções de humanização (humanization), como
transformar um número em uma duração legível para humanos ('três minutos
atrás') ou em uma frase. Ele funciona em python3, sendo recomendado
o uso da versão mais recente.

Este código é baseado no pacote original
[humanize](https://github.com/jmoiron/humanize), com atualização para
python3, correções de tradução, formato e adição de humanização de
listas. Além disso, foi retirado o recurso de localização (i18n)
facilitando sua utilização para português.

## Instalação

Para instalar o `humanizer-portugues` execute o comando:

```sh
pip install humanizer-portugues
```

## Uso

Para importar o pacote basta executar:

```python
import humanizer_portugues
```

Humanization de inteiros:

```python
humanizer_portugues.int_comma(12345)
'12,345'

humanizer_portugues.int_word(123455913)
'123.5 milhão'

humanizer_portugues.int_word(12345591313)
'12.3 bilhão'

humanizer_portugues.ap_number(4)
'quatro'

humanizer_portugues.ap_number(41)
'41'
```

Humanization datas e horas:

```python
import datetime
humanizer_portugues.natural_period(datetime.time(5, 30, 0).hour)
'manhã'

humanizer_portugues.natural_clock(datetime.time(0, 30, 0))
'zero hora e trinta minutos'

humanizer_portugues.natural_clock(datetime.time(0, 30, 0), formal=False)
'meia noite e meia'

humanizer_portugues.natural_day(datetime.datetime.now())
'hoje'

humanizer_portugues.natural_delta(datetime.timedelta(seconds=1001))
'16 minutos'

humanizer_portugues.natural_day(datetime.datetime.now() - datetime.timedelta(days=1))
'ontem'

humanizer_portugues.natural_day(datetime.date(2007, 6, 5))
'5 de junho'

humanizer_portugues.natural_date(datetime.date(2007, 6, 5))
'5 de junho de 2007'

humanizer_portugues.natural_time(datetime.datetime.now() - datetime.timedelta(seconds=1))
'há um segundo'

humanizer_portugues.natural_time(datetime.datetime.now() - datetime.timedelta(seconds=3600))
'há uma hora'
```

Humanization de tamanho de arquivos:

```python
humanizer_portugues.natural_size(1000000)
'1.0 MB'

humanizer_portugues.natural_size(1000000, binary=True)
'976.6 KiB'

humanizer_portugues.natural_size(1000000, gnu=True)
'976.6K'
```

Humanization de números de ponto flutuante:

```python
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
```

Humanization de listas:

```python
humanizer_portugues.natural_list(['Cláudio', 'Maria'], ',')
'Cláudio, Maria'

humanizer_portugues.natural_list(['Cláudio', 'Maria'], ',', 'e')
'Cláudio e Maria'

humanizer_portugues.natural_list(['Cláudio', 'Maria', 'José'], ';', 'ou')
'Cláudio; Maria ou José'
```
