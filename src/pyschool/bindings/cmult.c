// cmult.c
#include <stdio.h>
#include "cmult.h"

/*
This example from Real Python
https://realpython.com/python-bindings-overview/
binds a C++ multiplication function for use in Python.
The function, cmult, taes a an `int` and a `float` and returns a `float`.
Original source code at 
https://github.com/realpython/materials/blob/master/python-bindings/cmult.c
*/

float cmult(int int_param, float float_param)
{
    float return_value = int_param * float_param;
    printf("    In cmult: int: %d float %.1f returning  %.1f\n", int_param, float_param, return_value);
    return return_value;
}
