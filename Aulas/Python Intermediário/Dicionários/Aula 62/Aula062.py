# d1 = {'chave1': 'valor da chave'}
# print(d1)

"Atribuindo valore (tipo o append das listas)"

# d1 = {'chave1': 'valor da chave'}
# d1['Nova_chave'] = 'Valor da nova chave'
# print(d1)

# Outra forma:

# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# d1.update({'nova_chave': 'Valor da nova chave'})
# print(d1)


"""Printando o valor que você quiser """

# d1 = {'chave1': 'valor da chave'}
# d1['Nova_chave'] = 'Valor da nova chave'
# print(d1['chave1'])

"""Outra forma de criar dicionários"""

# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# d1['nova_chave'] = 'Valor da nova chave'

# print(d1)


# """Tuplas como chaves"""

# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }

# print(    d1[(1,2,3,4)]   )

"""Tentando printar uma chave que não existe no dicionário"""

# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }
# print(    d1['naoexiste']   ) # Receberá uma excessão

# sem dar erro:

# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }
# d1['nãoexiste'] = 'AGoraexiste =)'
# if 'naoexiste' in d1:
#     print(    d1['nãoexiste']   ) 

# Outra forma sem dar erro:

# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }

# print(    d1.get('naoexiste') ) # Saída == None

# Outra forma


# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }

# if d1.get('naoexiste') is not None:
#     print(d1.get('naoexiste'))

"""Excluindo chaves"""

# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }
# print(d1)

# del d1['str'] # Exluindo a chave "str"

# print(d1)

"""Checando se um valor e uma chave estão no dicionário"""

# d1 = {
#     'str':'valor',
#     123: 'Outro valor',
#     (1,2,3,4): 'Tupla'
# }

# print('str' in d1) # checando se uma chave está dentro de d1
# print('valor' in d1.values()) # checando se um valor está em d1

"""Iterando sobre as chaves dos dicionários (for)"""

# d1 = {
#     'chave1':'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla'
# }

# for key in d1:
#     print(key)

"""Iterando sobre os valores dos dicionários (for)"""

# d1 = {
#     'chave1':'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla'
# }

# for value in d1.values():
#     print(value)

"""Iterando sobre os valores e as chaves dos dicionários (for)"""

# d1 = {
#     'chave1':'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla'
# }

# for key, value in d1.items():
#     print(key, value)

# Outra forma:

# d1 = {
#     'chave1':'valor',
#     'chave2': 'Outro valor',
#     'chave3': 'Tupla'
# }

# for key in d1.items():
#     print(key) # aqui podemos usar key[0] para acessar a chave e key[1] para acessar o valor

"""Dicionários dentro de um dicionário"""

# clientes = {
#     'cliente1': {
#         'nome':'Denner',
#         'sobrenome':'Fernandes',
#     },
#     'cliente2': {
#         'nome':'João',
#         'sobrenome':'Moreira',
#     },
# }

# for clientes_key, clientes_value in clientes.items():
#     print(f'Exibindo {clientes_key}')
#     for dados_key, dados_value in clientes_value.items():
#         print(f'\t{dados_key} = {dados_value}')

"""Copiando dicionários de forma raza"""

# d1 = {1: 'a', 2: 'b', 3: 'c'}
# v = d1.copy()
# v[1] = 'Denner'
# print(v)
# print(d1)

# Outro exemplo

# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Denner', 'Fernandes']}
# v = d1.copy()
# v[1] = 'Denner'
# v['d'][0] = 'Joãozinho'

# print(v['d'][0])
# print(d1)
# print(v)

"""Copiando dicionários de forma completa"""

# import copy

# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Denner', 'Fernandes']}
# v = copy.deepcopy(d1)
# v[1] = 'Denner'
# v['d'][0] = 'Joãozinho'

# print(v['d'][0])
# print(d1)
# print(v)

"""transformando lista/tupla em dicionários"""
# lista = [
#     ['c1',1],
#     ['c2',2],
#     ['c3',3],
# ]
# d1 = dict(lista)
# print(d1)

# também é possivel fazer como tuplas dentro de lista ou lista dentro de tupla, exemplo:

# lista = [
#     ('c1',1),
#     ('c2',2),
#     ('c3',3),
# ]
# d1 = dict(lista)
# print(d1)

"""Eliminando chaves do dicionário"""

# d1 = {
#     1: 2,
#     2: 3,
#     4: 5,
# }

# d1.pop(4)
# print(d1)

"""Concatenando dois dicionários"""
d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d2 = {
    'a':'b',
    'c':'d',
}
d1.update(d2)
print(d1)
