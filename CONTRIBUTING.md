Contributing to humanizer-portugues
===================================

Sempre verifique crie, verifique os teestes unitários, mantendo a cobertura de código:

``` {.sourceCode .sh}
pip3 install codecov
coverage run --omit="*/tests/*" -m unittest discover # executa testes
coverage report # mostra cobertura
coverage html # gera site em html para ver a cobertura de cada linha
```
