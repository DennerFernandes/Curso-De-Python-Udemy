from random import randint

novo_cpf = str(randint(100000000, 999999999))
soma_dos_algarismos = soma_dos_algarismos_segundo =  0

for progressivo, regressivo in enumerate(range(10, 1, -1)):
    multiplicando = int(novo_cpf[progressivo]) * regressivo
    soma_dos_algarismos += multiplicando

calculo = 11 - (soma_dos_algarismos % 11)
digito_1 = 0 if calculo > 9 else calculo
novo_cpf += str(digito_1)

for progressivo, regressivo in enumerate(range(11, 1, -1)):
    multiplicando_segundo = int(novo_cpf[progressivo]) * regressivo
    soma_dos_algarismos_segundo += multiplicando_segundo

calculo_segundo = 11 - (soma_dos_algarismos_segundo % 11)

digito_2 = calculo_segundo if calculo_segundo<= 9 else 0
novo_cpf += str(digito_2)
print(novo_cpf)
