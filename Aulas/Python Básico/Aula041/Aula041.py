"""
Split, Join, Enumerate em python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumarete - Enumerar elementos da lista # list / iteráveis
"""
"""
Split
"""
# Exemplo 1 Split

# string = 'O Brasil é um país do futebol, o Brasil é penta.'
# lista = string.split(' ')
#
# print(lista)

# Exemplo 2 Split

# string = 'O Brasil é um país do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
# print(lista_2)

# Exemplo 3 Split

# string = 'O Brasil é um país do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# for valor in lista_1:
#     print(f'A palavra {valor} apareceu {lista_1.count(valor)}x  na frase')

# Exemplo 4 Split

# string = 'O Brasil é o o o país do futebol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
# contagem = 0
# palavra = ''
# for valor in lista_1:
#     quantidade_de_vezes = lista_1.count(valor)
#     if quantidade_de_vezes > contagem:
#         contagem = quantidade_de_vezes
#         palavra = valor
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

"""
Join
"""

# string = 'O Brasil é penta.'
# lista = string.split(' ')
# string2 = '_'.join(lista)
# print(string)
# print(lista)
# print(string2)

"""
Enumerate
"""

# string = 'O Brasil é penta.'
# lista = string.split(' ')
#
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])
