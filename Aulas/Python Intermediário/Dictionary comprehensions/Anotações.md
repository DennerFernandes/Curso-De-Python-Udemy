####Exemplo 1 de compreensão de dicionários (dictonary comprehensions):
```
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}
print(d1)
```
Saída:
```
{'chave': 'valor', 'chave2': 'valor2'}
```
####Exemplo 2
```
lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x.upper(): y.upper() for x, y in lista}
print(d1)
```
Saída:
```
{'CHAVE': 'VALOR', 'CHAVE2': 'VALOR2'}
```
#### Exemplo 3

```
d1 = {x: y for x, y in enumerate(range(5))}
print(d1)
```
Saída:
```
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4}
```
#### Exemplo 4 (Com sets)

```
d1 = {x for x in range(5)}
print(d1, type(d1))
```
Saída:
```
{0, 1, 2, 3, 4} <class 'set'>
```
#### Exemplo 5
```
d1 = {f'chave_{x}': x**2 for x in range(5)}
print(d1)
```
Saída:
```
{'chave_0': 0, 'chave_1': 1, 'chave_2': 4, 'chave_3': 9, 'chave_4': 16}
```
