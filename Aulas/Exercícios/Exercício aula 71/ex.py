carrinho = list()

while True:
    produto_informado = input('Informe o nome do produto: ')
    preco_do_produto_informado = int(input('Informe o preço do produto: '))

    carrinho.append((produto_informado, preco_do_produto_informado))

    continuar = input('Quer continuar? [S/N] ').lower()
    print('-'*30)
    if continuar == 'n':
        break

somando_os_precos = sum([valor[1] for valor in carrinho])
print(f'A soma dos preços do seu carrinho é {somando_os_precos}')





