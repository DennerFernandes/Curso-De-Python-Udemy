############ Exercício 1 ############ 

print('-'*30)
print('Exercício 1'.center(30))
print('-'*30)

numero =  input('Digite um número: ')


if numero.isdigit():
    numero1 = int(numero)
    if numero1 % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
else:
    print('Por favor, repita o programa e digite números inteiros válidos')

############  Ex 2 ############ 

print('-'*30)
print('Exercício 2'.center(30))
print('-'*30)

horario = input('Qual o horário atual? ')

if horario.isdigit():
    horario = int(horario)
    if horario <= 11:
        print('Bom dia!')
    elif 17 >= horario >= 12:
        print('Boa tarde!')
    elif horario >= 18:
        print('Boa noite!')
else:
    print('Horário inválido.')

############ Ex 2 ############ 

print('-'*30)
print('Exercício 3'.center(30))
print('-'*30)

nome = input('Digite seu primeiro nome: ')

if len(nome) <= 4:
    print('Seu nome é curto')
elif len(nome) <= 6:
    print('Seu nome é normal')
elif len(nome) > 6:
    print('Seu nome é muito grande')
