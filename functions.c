/* functions.c */
//
//gcc -dynamiclib -o libfunctions.dylib functions.c
//
#include <stdio.h>
#include <stdlib.h>

int fibRec(int n){
    if(n < 2)
        return n;
    else
        return fibRec(n-1) + fibRec(n-2);
}
