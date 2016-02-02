#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 2/Feb/16 14:08

"""
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("fibRec_Cython.pyx")
)
