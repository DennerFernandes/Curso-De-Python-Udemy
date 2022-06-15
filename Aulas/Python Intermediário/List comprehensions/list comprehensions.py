# Exemplo 1

# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [variavel for variavel in l1]
# print(l2)

# Exemplo 2

# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [variavel*2 for variavel in l1]
# print(l2)

# Exemplo 3
#
# l1 = [1,2,3,4,5,6,7,8,9]
# l2 = [(variavel,variavel2) for variavel in l1 for variavel2 in range(3)]
# print(l2)

# Exemplo 4

# l1 = ['Luiz', 'Mauro', 'Maria']
# l2 = [v.replace('a', '@').upper() for v in l1]
# print(l2)

# Exemplo 4

# tupla = (
#  lesga   ('chave', 'valor'),
#     ('chave2', 'valor2'),
# )
# l2 = [(y, x) for x, y in tupla]
# print(l2)

# Exemplo 5

# l1 = list(range(0,100))
# l2 = [v for v in l1 if v % 2 == 0]
#
# print(l2)

# Exemplo 6

# l1 = list(range(0,100))
# l2 = [v for v in l1 if v % 3 == 0 if v % 8 == 0]
# print(l2)

# Exemplo 7

# l1 = list(range(100))
# l2 = [v if v % 3 == 0 else 'Não é' for v in l1]
# print(l2)
