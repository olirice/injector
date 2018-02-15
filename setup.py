#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import re
import os
import sys


def get_version():
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open('injector.py').read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version()


setup(
    name='injector',
    version=version,
    url='http://github.com/olirice/injector',
    license='BSD',
    description='Dependency injection for python.',
    author='Oliver Rice',
    author_email='oliver@oliverrice.com',
    py_modules=['injector'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
