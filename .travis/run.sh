#!/bin/bash

set -e
set -x

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    PYENV_ROOT="$HOME/.pyenv-humanizer-portugues"
    PATH="$PYENV_ROOT/bin:$PATH"
    hash -r
    eval "$(pyenv init -)"
fi
REQUIRE_SPEEDUPS=1 python setup.py build_ext -i
python -m compileall -f .
coverage run -m unittest discover

if [[ $TRAVIS_OS_NAME == 'osx' ]]; then
    python setup.py bdist_wheel
fi

if [[ $BUILD_SDIST == 'true' ]]; then
    python setup.py sdist
fi
