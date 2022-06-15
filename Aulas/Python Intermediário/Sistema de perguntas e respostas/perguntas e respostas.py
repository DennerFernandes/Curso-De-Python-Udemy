perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '2',
            'b': '3',
            'c': '5',
            'd': '4'
        },
        'resposta_correta': 'd'
    },
    'Pergunta 2': {
        'Pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '10','b': '4','c': '8','d': '6'},
        'resposta_correta': 'd',
    },
    }

respostas_certas = 0
print()

for chave_pergunta, valor_pergunta in perguntas.items():
    print(f'{chave_pergunta}: {valor_pergunta["Pergunta"]}')

    for chave_da_resposta, valor_da_resposta in valor_pergunta['respostas'].items():
        print(f'{chave_da_resposta}: {valor_da_resposta}')

    resposta_user = input('Sua resposta: ')

    if resposta_user == valor_pergunta['resposta_correta']:
        print(f'️Parabéns, você acertou!!!')
        respostas_certas += 1
    else:
        print(f'\033[31mX\033[m Você errou! A resposta correta era "{valor_pergunta["resposta_correta"]}"')

    print()

quantidade_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_perguntas * 100

print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto:.0f}%.')
