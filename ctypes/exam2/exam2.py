import ctypes

class CExample(ctypes.Structure):
    _fields_ = [
        ('data', ctypes.POINTER(ctypes.c_char)),
        ('len', ctypes.c_int),
        ('doubles', ctypes.POINTER(ctypes.c_double)),
        ('count', ctypes.c_int)]

    def __init__(self, length, count):
        self.data = ctypes.cast(ctypes.create_string_buffer(length), ctypes.POINTER(ctypes.c_char))
        self.len = length
        self.doubles = (ctypes.c_double * count)()
        self.count = count
    
    def __repr__(self):
        return 'Example({},[{}]'.format(
            ctypes.string_at(self.data),
            ','.join(str(self.doubles[i]) for i in range(self.count)) )
    
class CDll:
    def __init__(self):
        self.dll = ctypes.CDLL('exam2.dll')
        self.dll.func.argtypes = [ctypes.POINTER(CExample)]
        self.dll.func.restype = None

    def func(self, ex):
        self.dll.func(ctypes.byref(ex))


if __name__ == '__main__':
    d = CDll()
    e = CExample(20, 5)
    print('before', e)
    d.func(e)
    print('after', e)

    intc = ctypes.c_int(100)
    p_int_c = ctypes.pointer(intc)
    print(intc.value)
    print(ctypes.byref(intc))
    print p_int_c.contents, p_int_c.contents.value

    p_example_e = ctypes.pointer(e)
    print ctypes.string_at(p_example_e.contents.data)
    print p_example_e.contents.count

    a = (ctypes.c_byte * 5) ()
    print a

    ctypes.cast(a, ctypes.POINTER(ctypes.c_int))
    print a