import os
from ctypes import *
from platform import *

dll_names = {
    'Windows': 'msvcrt.dll',
    'Linux': 'libc.so.6'
    }

libc = cdll.LoadLibrary(dll_names[system()])
printf = libc.printf
printf("Hello, %s's printf.\n", system())
printf(c_char_p("Hello c_int(%d) c_double(%f)\n"), c_int(15), c_double(3.14))

p_str = c_char_p()
int_val = c_int()
double_val = c_double()

p_str.value = "Hello World - %d, %f\n"
int_val.value = 16
double_value = 12.3
printf(p_str, int_val, double_val)

type_p_int = POINTER(c_int)
v = c_int(7)
p_int = type_p_int(v)

print(type(p_int))
print(p_int)
print(p_int.contents)
print(v)

filepath = os.path.dirname(os.path.abspath(__file__))
dllpath = os.path.join(filepath, 'exam1.dll')
myDll = cdll.LoadLibrary(dllpath)

print(myDll.get_inc(5))
myArray_t = c_int * 5
myArray = myArray_t(5, 1, 13, 17, 23)
print(myDll.get_array_value(myArray, 3))

p = create_string_buffer("Hello", 10)
print sizeof(p), ',', repr(p.raw)

