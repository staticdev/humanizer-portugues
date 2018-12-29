#!/usr/bin/env python
import codecs
import os.path
import re
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

long_description = read('README.md')
requires = []

setup(
    name='humanizer-portugues',
    version=find_version("humanizer_portugues", "__init__.py"),
    description="Funcoes para humanizacao (humanize) para python ",
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    keywords='humanize portugues data hora tamanho',
    maintainer='Thiago Carvalho D Avila',
    maintainer_email='thiagocavila@gmail.com',
    url='https://github.com/staticdev/humanizer-portugues',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    tests_require=['mock'],
    install_requires=requires,
)
