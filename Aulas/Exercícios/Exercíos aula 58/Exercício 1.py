def ola_mundo():
    return 'Olá mundo!'

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)
