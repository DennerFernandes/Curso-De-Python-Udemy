"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range

Sumário:
Obs: O número que se encontra depois do traço é a linha em que está cada coisa

Alterando indices - 25
Fatiamento - 33
Concatenando listas - 41
Extend - 52
Append - 62
Insert - 73
Del - 84
Max e Min - 92
Range - 100
For com listas - 107
Jogo de adivinhação - 116
"""

"""
Alterando indices
"""
# #        0    1    2    3    4    5
# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# lista[5] = 'Qualquer outra coisa'
# print(lista[5])

"""
Fatiamento
"""

# lista = ['A', 'B', 'C', 'D', 'E', 10.5]
# print(lista[:3])
# print(lista[::-1])

"""
Concatenando listas
"""

# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_3 = lista_1 + lista_2
# print(lista_1)
# print(lista_2)
# print(lista_3)

"""
Extend
"""

# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_1.extend(lista_2)
# print(lista_1)
# print(lista_2)

"""
Append
"""

# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# lista_2.append('b')
#
# print(lista_1)
# print(lista_2)

"""
Insert
"""
# lista_1 = [1, 2, 3]
# lista_2 = [4, 5, 6]
# print(lista_2)
# lista_2.insert(0, 'banana')
# print(lista_2)
# lista_2.pop()
# print(lista_2)

"""
Del
"""

# lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# del(lista_2[3:5])
# print(lista_2)

"""
Max e Min
"""

# lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lista_2))
# print(min(lista_2))

"""
Range
"""

# lista_2 = list(range(1, 10))
# print(lista_2)

"""
For com listas
"""
# lista_2 = list(range(1, 100, 8))
# soma = 0
# for valor in lista_2:
#     soma += valor
# print(soma)

"""
Jogo de adivinhação
"""

# secreto = 'perfume'
# digitados = []
# chances = 3
#
# while True:
#     if chances <= 0:
#         print('Você perdeu!!!')
#         break
#     letra = input('Digite uma letra: ')
#     if len(letra) > 1:
#         print('Ahhh isso não vale, digite apenas uma letra')
#         continue
#     digitados.append(letra)
#     if letra in secreto:
#         print(f'Ótimo chute! A letra {letra} existe na palavra secreta.')
#     else:
#         print(f'Aff. A letra {letra} não está na palavra secreta')
#         digitados.pop()
#
#     secreto_temporario = ''
#     for letra_secreta in secreto:
#         if letra_secreta in digitados:
#             secreto_temporario += letra_secreta
#         else:
#             secreto_temporario += '*'
#     if secreto_temporario == secreto:
#         print(f'Parabéns! Você ganhou!! A palavra era {secreto}')
#         break
#     else:
#         print(f'A palavra secreta está assim: {secreto_temporario}')
#     if letra not in secreto:
#         chances -= 1
#     print(f'Você ainda tem {chances} chances')
#     print()