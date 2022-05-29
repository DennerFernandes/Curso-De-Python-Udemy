--------------------->>> Dicionários <<<---------------------

Para criar um dicionário, utilizamos chaves "{}", veja:
```
d1 = {}
```
Para atribuir valores ao dicionário, escrevemos a chave, seguido de dois pontos ":", seguido do valor da chave.
Exemplo:
```
d1 = {'chave1': 'valor da chave'}
```
Para atribuir um valor, fora do dicionário (tipo o append das listas), fazemos o seguinte:
```
d1 = {'chave1': 'valor da chave'}
d1['Nova_chave'] = 'Valor da nova chave'
```
Retorna:
```
{'chave1': 'valor da chave', 'Nova_chave': 'Valor da nova chave'}
```
Para printar o valor que você deseja no dicionário (tipo os indices da lista), fazemos assim:
```
d1 = {'chave1': 'valor da chave'}
d1['Nova_chave'] = 'Valor da nova chave'
print(d1['chave1'])
```
Retorna:
```
valor da chave
```
Outro jeito de criar dicionário é o seguinte:
```
d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
```
As chaves dos dicionários podem receber qualquer valor imutável, ou seja, inteiro, strings até tuplas.
Exemplo:
```
d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}
print(    d1[(1,2,3,4)]   )
```
Retorna:
```
Tupla
```
Se você tentar printar uma chave que não exista, receberá a seguinte excessão:

