#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os.path
import re
import setuptools


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    """Gets version on __init__.py"""
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name='humanizer-portugues',
    version=find_version("humanizer_portugues", "__init__.py"),
    description="Funções para humanização (humanize) para python ",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
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
    packages=setuptools.find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite="tests",
    tests_require=['mock'],
    install_requires=[],
)
