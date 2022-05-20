numero1 =  input('Digite um número: ')
numero2 =  input('Digite um outro número: ')


if numero1.isdigit() and numero2.isdigit():

    if numero1 % 2 == 0:
        print(f'O número {numero1} é par')
    else:
        print(f'O número {numero1} é ímpar')


    if numero2 % 2 == 0:
        print(f'O número {numero2} é par')
    else:
        print(f'O número {numero2} é ímpar')
else:
    print('Por favor, repita o programa e digite números inteiros válidos')

############ Ex 2 ############ 

print()
horario = input('Qual o horário atual? ')
if horario.isnumeric():
    horario = int(horario)
    if horario > 11:
        print('Bom dia!')