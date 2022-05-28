"""
Funções (def) em python -  *args **kwargs (Parte 3)
"""

# lista = [1,2,3,4,5]
# print(*lista, sep='-')
# """Sep separa os valores do desempacotamento de lista de acordo com o que está entre aspas"""

# --------------------
"""Usando args"""


# def func(*args):
#     args = list(args) # Aqui transformamos args em uma lista, em vez de uma tupla
#     args[0] = 20
#     print(args)
#
#
# func(1,2,3,4,5)

# --------------------

# def func(*args):
#     print(args)
#
#
# lista = [1,2,3,4,5]
# func(*lista,10,20,40,50) # Aqui mandamos a lista desempacotada apara os indices da tupla que está em *args

"""Usando kwargs"""

#
# def func(*args, **kwargs):
#     print(args)
#     idade = kwargs.get('idade')
#     if idade is not None:
#         print(idade)
#     else:
#         print('idade não existe')
#
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,40,50]
# func(*lista,*lista2, nome='Denner', sobrenome='Fernandes', idade=13)


