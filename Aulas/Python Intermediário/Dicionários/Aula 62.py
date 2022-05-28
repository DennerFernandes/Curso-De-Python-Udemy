# d1 = {'chave1': 'valor da chave'}
# print(d1)

"Atribuindo valore (tipo o append das listas)"

# d1 = {'chave1': 'valor da chave'}
# d1['Nova_chave'] = 'Valor da nova chave'
# print(d1)

"""Printando o valor que você quiser """

# d1 = {'chave1': 'valor da chave'}
# d1['Nova_chave'] = 'Valor da nova chave'
# print(d1['chave1'])

"""Outra forma de criar dicionários"""

# d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
# d1['nova_chave'] = 'Valor da nova chave'

# print(d1)

"""Tuplas como chaves"""

d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}
print(    d1[(1,2,3,4)]   )
