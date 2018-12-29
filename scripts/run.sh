#!/bin/bash
set -e
set -x
 
REQUIRE_SPEEDUPS=1 python setup.py build_ext -i
python -m compileall -f .
coverage run --omit="*/tests/*" -m unittest discover

if [[ $BUILD_SDIST == 'true' ]]; then
    python setup.py sdist
fi