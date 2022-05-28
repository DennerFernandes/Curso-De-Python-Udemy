# a = lambda x,y: x * y
# print(a(2,2))

"""Outro exemplo"""

# lista = [
#     ['Produto 1', 13],
#     ['Produto 2', 6],
#     ['Produto 3', 7],
#     ['Produto 4', 50],
#     ['Produto 5', 8]
# ]

# # Ordenando a lista

# def funcao(item):
#     return item[1]
#
# lista.sort(key=funcao)
# print(lista)

# Usando lambda

# lista = [
#     ['Produto 1', 13],
#     ['Produto 2', 6],
#     ['Produto 3', 7],
#     ['Produto 4', 50],
#     ['Produto 5', 8]
# ]
# lista.sort(key=lambda item: item[1])
# print(lista)

# Usando sorted

# lista = [
#     ['Produto 1', 13],
#     ['Produto 2', 6],
#     ['Produto 3', 7],
#     ['Produto 4', 50],
#     ['Produto 5', 8]
# ]

# print(sorted(lista, key=lambda i:i[1]))
# print(lista)


"""Outro exemplo"""

# preco = 500
# def calcular_imposto(preco):
#     return preco * 0.3

# print(calcular_imposto(preco))

# Com expreções lambda

# preco = 1000

# calcular_imposto2 = lambda x: x * 0.3
# print(calcular_imposto2(preco))

"""Outro exemplo"""

# precos = [100,500,10,25]
# impostos = list(map(lambda x: x * 0.3, precos))
# print(impostos)