#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
longqi 1/Feb/16 20:55

"""
from ctypes import *
import timeit

# import pyximport
# pyximport.install()

# import fibRec_Cython
import fibRec_Cython

# import fibRec_C
CLib = cdll.LoadLibrary("./libfunctions.dylib")


def fibRec_Python(n):
    if n < 2:
        return n
    else:
        return fibRec_Python(n - 1) + fibRec_Python(n - 2)


number = 32

# Python 3 Fibonacci
print("Python\t:",
      min(timeit.Timer(stmt='x = fibRec_Python(number)',
                       setup='from __main__ import fibRec_Python, number').repeat(repeat=10,
                                                                                  number=1)))

# Cython Fibonacci
print("Cython\t:",
      min(timeit.Timer(stmt='x = fibRec_Cython.fibRec(number)',
                       setup='from __main__ import fibRec_Cython, number').repeat(repeat=10,
                                                                                  number=1)))

# C Fibonacci
print("C lib\t:",
      min(timeit.Timer(stmt='x = CLib.fibRec(number)',
                       setup='from __main__ import CLib, number').repeat(repeat=10,
                                                                         number=1)))
