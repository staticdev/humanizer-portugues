# Contributing to humanizer-portugues

- Install [Poetry](https://python-poetry.org/)
- Create a fork and clone it
- Change and create unit tests
- Verify:

```sh
pip3 install codecov
coverage run --omit="*/tests/*" -m unittest discover # executa testes
coverage report # mostra cobertura
coverage html # gera site em html para ver a cobertura de cada linha
```
