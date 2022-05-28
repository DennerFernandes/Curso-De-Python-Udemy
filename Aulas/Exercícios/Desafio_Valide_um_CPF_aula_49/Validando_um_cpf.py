cpf = input('Informe seu CPF: ').strip().replace('.', '').replace('-', '')
primeiros_números_do_cpf = cpf[:-2]
soma_dos_algarismos = soma_dos_algarismos_segundo =  0

# Primeiro dígito depois do traço

for progressivo, regressivo in enumerate(range(10, 1, -1)):
    multiplicando = int(primeiros_números_do_cpf[progressivo]) * regressivo
    soma_dos_algarismos += multiplicando

calculo = 11 - (soma_dos_algarismos % 11)

digito_1 = 0 if calculo > 9 else calculo

# Segundo dígito depois do traço

lista_com_os_digitos_e_o_cpf = primeiros_números_do_cpf + str(digito_1)

for progressivo, regressivo in enumerate(range(11, 1, -1)):
    multiplicando_segundo = int(lista_com_os_digitos_e_o_cpf[progressivo]) * regressivo
    soma_dos_algarismos_segundo += multiplicando_segundo

calculo_segundo = 11 - (soma_dos_algarismos_segundo % 11)

digito_2 = calculo_segundo if calculo_segundo<= 9 else 0

novo_cpf = f'{primeiros_números_do_cpf}{str(digito_1)}{str(digito_2)}'

cpf_valido_ou_invalido = f'O cpf {novo_cpf} é válido' if cpf == novo_cpf else f'O cpf {cpf} é inválido'
print(cpf_valido_ou_invalido)