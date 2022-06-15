# Exemplo 1

# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# ]
# d1 = {x: y for x, y in lista}
# print(d1)

# Exemplo 2

# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# ]
# d1 = {x.upper(): y.upper() for x, y in lista}
# print(d1)

# Exemplo 3

# d1 = {x: y for x, y in enumerate(range(5))}
# print(d1)

# Exemplo 4 (Com sets)

# d1 = {x for x in range(5)}
# print(d1, type(d1))

# Exemplo 5

d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)
