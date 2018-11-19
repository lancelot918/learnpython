import ctypes
from ctypes import *
from ctypes.util import find_library

class CPoint(ctypes.Structure):
    _fields_ = [
        ('x', ctypes.c_double),
        ('y', ctypes.c_double),
    ]

class CTest(ctypes.Structure):
    _fields_  = [
        ('sentence', ctypes.c_char_p),
        ('nb_points', ctypes.c_int),
        ('points', ctypes.POINTER(CPoint)),
        ('distances', ctypes.POINTER(c_double)),
    ]

libc = ctypes.CDLL(find_library('c'))
libc.free.argtypes = [ctypes.c_void_p]
libc.free.restype = ctypes.c_void_p

libmsq = cdll.LoadLibrary('msq.dll')
libmsq.increment_string.argtypes = [ctypes.c_char_p, ctypes.c_int]
libmsq.increment_string.restype = ctypes.c_char_p
libmsq.generate_points.argtypes = [ctypes.POINTER(CTest), ctypes.c_int]
libmsq.distance_between_points.argtypes = [ctypes.POINTER(CTest)]

if __name__ == '__main__':
    test = {}
    test['sentence'] = "A nice sentence to test.".encode('utf-8')
    test['nb_points'] = 0
    test['points'] = None
    test['distances'] = None

    c_test = CTest(**test)
    p_test = ctypes.pointer(c_test)

    libmsq.generate_points(p_test, 10000)
    p_test.contents.sentence = libmsq.increment_string(p_test.contents.sentence, -5)
    print(test['sentence'])
    libmsq.distance_between_points(p_test)
    #libc.free(p_test.contents.points)
    #libc.free(p_test.contents.distances)    
