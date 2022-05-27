"""
While em python - Aula 34
utilizado para realizar ações enquanto
uma condição for verdadeira.

Requisitos: Entender Condições e operadores
"""

"""
Exemplo 1
"""
# while True: # loop infinito
#     nome = input('Qual seu nome? ')
#     print(f'Olá {nome}!')

"""
Exemplo 2
"""

# x = 0
# while x < 5:
#     print(x)
#     x += 1
# print('Acabou!')

"""
Palavra continue

A palavra continue, sempre que estiver 
dentro de um laço, o interpretador do 
python, ele vai recomeçar o laço
"""

# x = 0
# while x < 10:
#     if x == 3:
#         x = x + 1
#         continue
#     print(x)
#     x += 1
# print('Acabou!')

""" 
Palavra break

A a palavra break quebra o código, ou seja, finaliza o loop quando
determinada condição for verdadeira
"""

x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break
    print(x)
    x += 1
print('Acabou!')

""" 
Exemplo 3
"""

# x = 0 # coluna
# while x < 10:
#     y = 0 # linha
#     while y < 5:
#         print(f'X vale {x} e Y vale {y}')
        
#         y += 1
#     x += 1
# print('Acabou!')

"""
Calculadora
"""

# while True:
#     print()
#     num_1 = input('Digite um número: ')
#     num_2 = input('Digite outro número: ')
#     operador = input('Digite um operador: ')
#     sair = input('Deseja sair? [S/N] ')
#     if not num_1.isnumeric() or not num_2.isnumeric():
#         print('Você pecisa digitar um número.')

#     if sair == 's':
#         break
#     num_1 = int(num_1)
#     num_2 = int(num_2)

    
#     if operador == '+':
#         print(num_1 + num_2)
#     elif operador == '-':
#         print(num_1 - num_2)
#     elif operador == '/':
#         print(num_1 / num_2)
#     elif operador == '*':
#         print(num_1 * num_2)
#     else:
#         print('Operador inválido')

