# speedup_python
Using C and Cython to speedup your python

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
