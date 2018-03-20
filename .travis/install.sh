#!/bin/bash

set -e
set -x

pip3 install codecov

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    if [ ! -e "$HOME/.pyenv-humanizer-portugues/.git" ]; then
      if [ -e "$HOME/.pyenv-humanizer-portugues" ]; then
        rm -rf ~/.pyenv-simplejson
      fi
      git clone https://github.com/yyuu/pyenv.git ~/.pyenv-humanizer-portugues
    else
      (cd ~/.pyenv-humanizer-portugues; git pull)
    fi
    PYENV_ROOT="$HOME/.pyenv-humanizer-portugues"
    PATH="$PYENV_ROOT/bin:$PATH"
    hash -r
    eval "$(pyenv init -)"
    hash -r
    pyenv install --list
    pyenv install -s $PYENV_VERSION
    pip install wheel
fi
