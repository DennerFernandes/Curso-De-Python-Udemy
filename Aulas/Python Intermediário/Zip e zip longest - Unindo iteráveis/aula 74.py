"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""

# Zip

# cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
# estados = ['SP', 'MG', 'BA']
#
# cidades_estados = zip(estados, cidades)
#
# for valor in cidades_estados:
#     print(valor)


# Zip Longest

from itertools import zip_longest

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip_longest(estados, cidades, fillvalue='MG')

for valor in cidades_estados:
    print(valor)

# Usando 3 listas

# from itertools import zip_longest,count
#
# indice = count()
# cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
# estados = ['SP', 'MG', 'BA']
#
# cidades_estados = zip(indice, estados, cidades)
#
# for valor in cidades_estados:
#     print(valor)
