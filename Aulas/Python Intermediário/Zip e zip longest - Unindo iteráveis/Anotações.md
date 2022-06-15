#### Função **zip()**
A função `zip()` já vem com o python, ou seja, não é necessário importar ou baixar alguma biblioteca disponível.

A função `zip()` basicamente junta quantos iteráveis você passar como parâmetro, ou seja, irá juntar o indice 1 da lista 1 com o indice 1 da lista 2, por exemplo.
Uma coisa de que não se pode esquecer, é que a ordem em que você quer que as listas se juntem é importante, por isso deve-se sempre passar os parâmetros na ordem correta.

Veja o exemplo a seguir:
```
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados, cidades)

for estado, cidade in cidades_estados:
    print(estado, cidade)
```
Saída:
```
SP São Paulo
MG Belo Horizonte
BA Salvador
```
Podemos ver que aconteceu exatamente o que eu disse ali em cima: A função `zip()` juntou as duas listas, indice a indice (lista 1 indice 1 com lista 2 indice 2 e assim por diante até acabar a lista), transformando-os em uma tupla contendo o `estado` e a `cidade` permitindo, assim, iterar sobre seus elementos.
Outra coisa é que a função `zip()` é um gerador, ou seja, ela ocupa muito menos espaço na memória do que uma lista.
Podemos observar que, a cidade de `Monte Belo` não foi adicionada a nenhuma tupla, isso porque `zip()` só itera até o final da menor lista, ou seja, ele fez o seguinte:

```
indice 0 de estados, com indice 0 de cidades
indice 1 de estados, com indice 1 de cidades
indice 2 de estados, com indice 2 de cidades
```
Daí, nesse ponto, a menor lista ja acabou, então ele simplesmente ignora o último valor da lista de `cidades`. Para podermos juntar `Monte  Belo` também, devemos usar a função `zip_longest`.

#### Função zip_longest()

Para usara função `zip_longest()` devemos importar uma biblioteca chamada `itertools`
