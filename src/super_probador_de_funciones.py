import ctypes as C
from random import randint, random

libmagic = C.CDLL('./libmagic.so')

# Seteando entrada y salida para add_floar y add_int
libmagic.add_float.restype = C.c_float
libmagic.add_float.argtypes = [C.c_float, C.c_float]

libmagic.add_int.restype = C.c_int
libmagic.add_int.argtypes = [C.c_int, C.c_int]

# Testeandolas a add_floar y add_int
numero_int, otro_numero_int = randint(1, 100), randint(1, 100)
numero_float, otro_numero_float = random(), random()

resultado_float = libmagic.add_float(numero_float, otro_numero_float)
print numero_float, '+', otro_numero_float, '=', resultado_float

resultado_int = libmagic.add_int(numero_int, otro_numero_int)
print numero_int, '+', otro_numero_int, '=', resultado_int


