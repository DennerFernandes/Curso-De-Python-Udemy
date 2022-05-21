"""
Aula 32 - Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO) f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^) (QUANTIDADE)(TIPO-s, d ou f)
ljust - ljust joga o nome a direita e preeche o resto com os caracteres informados
> - Esquerda
< - Direita
^ - Centro
"""


num_1 = 10
num_2 = 3
divisao = num_1 / num_2
print(f'{divisao}')
print('{}'.format(divisao))

###########################

nome = 'Luiz Otávio'
print(f'{nome:s}')

"""
Ex de utilização do:  
:(CARACTERE)(> ou < ou ^) (QUANTIDADE)(TIPO-s, d ou f)
"""
num_1 = 1
print(f'{num_1:0>10}')


num_2 = 1150
print(f'{num_2:0<10}')


num_3 = 1150
print(f'{num_2:.2f}')

###########################

nome = 'Otávio Miranda'
print(f'{nome:#^50}')

###########################

nome = 'Otávio'
sobrenome = 'Miranda'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

###########################
"""
ljust - ljust joga o nome a direita e preeche o resto com os caracteres informados
"""
nome = 'Luiz Otávio'
nome = nome.ljust(20, '#')
print(nome)

