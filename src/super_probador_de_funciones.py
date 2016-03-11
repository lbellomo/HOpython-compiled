import ctypes as C
import numpy as np 
from random import randint, random

libmagic = C.CDLL('./libmagic.so')

# Seteando entrada y salida para add_float y add_int
libmagic.add_float.restype = C.c_float
libmagic.add_float.argtypes = [C.c_float, C.c_float]

libmagic.add_int.restype = C.c_int
libmagic.add_int.argtypes = [C.c_int, C.c_int]

# Testeandolas a add_float y add_int
numero_int, otro_numero_int = randint(1, 100), randint(1, 100)
numero_float, otro_numero_float = random(), random()

print 'sumando con add_float:'
print '-' * 22
resultado_float = libmagic.add_float(numero_float, otro_numero_float)
print numero_float, '+', otro_numero_float, '=', resultado_float

print 'sumando con add_int:'
print '-' * 20
resultado_int = libmagic.add_int(numero_int, otro_numero_int)
print numero_int, '+', otro_numero_int, '=', resultado_int

# Testeando add_float_ref, add_int_ref
c_numero_int, c_otro_numero_int = C.c_int(numero_int), C.c_int(otro_numero_int)
c_res_int = C.c_int()
c_numero_float = C.c_float(numero_float)
c_otro_numero_float = C.c_float(otro_numero_float)
c_res_float = C.c_float()

libmagic.add_float_ref(C.byref(c_numero_float),
                       C.byref(c_otro_numero_float),
                       C.byref(c_res_float))

print 'Ahora usando punteros!'
print c_res_float.value, 'que nos da igual que', resultado_float

libmagic.add_int_ref(C.byref(c_numero_int),
                     C.byref(c_otro_numero_int),
                     C.byref(c_res_int))

print c_res_int.value, 'este otro tambien es igual a',resultado_int, 'que suerte!'

intp = C.POINTER(C.c_int)

array_int1 = np.array([randint(1, 100), randint(1, 100),
                       randint(1, 100)], dtype=C.c_int)
array_int2 = np.array([randint(1, 100), randint(1, 100),
                       randint(1, 100)], dtype=C.c_int)
array_int_out = np.zeros(3, dtype=np.int32)

libmagic.add_int_array(array_int1.ctypes.data_as(intp),
                       array_int2.ctypes.data_as(intp),
                       array_int_out.ctypes.data_as(intp),
                       C.c_int(3))

print 'Sumando arrays: ', array_int1, ' + ', array_int2, '=', array_int_out

array_float1 = np.array([random(), random(), random()], dtype=C.c_float)
array_float2 = np.array([random(), random(), random()], dtype=C.c_float)
# Se setea la funcion para que devuelva un float
libmagic.dot_product.restype = C.c_float
res_float = C.c_float(0)
res_float = libmagic.dot_product(array_float1.ctypes.data_as(intp),
                                    array_float2.ctypes.data_as(intp),
                                    C.c_int(3))
print 'Haciendo matematica mas posta con flotantes: ', '\n', array_float1, ' *' ,\
    '\n', array_float2, '\n', ' = ', res_float

print 'Donde numpy nos dice que da: ', np.dot(array_float1, array_float2)