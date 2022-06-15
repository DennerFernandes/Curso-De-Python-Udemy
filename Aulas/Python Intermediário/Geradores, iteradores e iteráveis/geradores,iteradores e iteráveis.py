"""
Iteráveis
"""

# lista = [0,1,2,3,4,5]
# string = 'String'
# print(hasattr(string, '__iter__'))

"""
Iteradores
"""

# lista = [0,1,2,3,4,5]
# lista = iter(lista)
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(hasattr(lista, '__next__'))

"""
Geradores
"""
# Exemplo 1

# import time
#
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
#
# for v in g:
#     print(v)

# Exemplo 2

# def gera():
#     variavel = 'Valor 1'
#     yield variavel
#     variavel = 'Valor 2'
#     yield variavel
#     variavel = 'Valor 3'
#     yield variavel
#
# g = gera()
# print(next(g))
# print(next(g))
# print(next(g))

import sys
import time

l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))

