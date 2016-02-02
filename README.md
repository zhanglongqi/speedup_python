# speedup_python
Using C and Cython to speedup your python

Thanks this [blog:](http://www.maxburstein.com/blog/speeding-up-your-python-code/)

1. Compile C file to dynamic shared library

   In Mac: `gcc -dynamiclib -o libfunctions.dylib functions.c`

   In Linux: `gcc -Wall -fPIC -shared -o libfunctions.so functions.c`

2. Compile Cython file
    There are two ways to do this:
    1. `python3 setup.py build_ext --inplace`
        This will generate .o and .so file. Then `import fibRec_Cython` in the caller

    2. using `pyximport`
        In the caller:
        ``` python
        import pyximport
        pyximport.install()
        import fibRec_Cython
        ```

3. `python3 main.py`



Result on my machine:
```
Python	: 0.8736008979976759
Cython	: 0.25456177699379623
C  lib	: 0.013578268997662235
```
