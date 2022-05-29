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
Saída:
```
{'chave1': 'valor da chave', 'Nova_chave': 'Valor da nova chave'}
```
Outra forma seria:
```
d1 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
d1.update({'nova_chave': 'Valor da nova chave'})
print(d1)
```
Saída:
```
{'chave1': 'Valor da chave', 'chave2': 'Valor da outra chave', 'nova_chave':'Valor da nova chave'}
```

Para printar o valor que você deseja no dicionário (tipo os indices da lista), fazemos assim:
```
d1 = {'chave1': 'valor da chave'}
d1['Nova_chave'] = 'Valor da nova chave'
print(d1['chave1'])
```
Saída:
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
Saída:
```
Tupla
```
Se você tentar printar uma chave que não exista, receberá a seguinte excessão:
```
Traceback (most recent call last):
  File "c:/CursoDePythonUdemy/Aulas/Python Intermediário/Dicionários/Aula 62.py", line 40, in <module>
    print(    d1['naoexiste']   ) # Receberá uma excessão
KeyError: 'naoexiste'
```
Para excluir uma chave, basta fazer assim:
```
d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}
print(d1)

del d1['str'] # Exluindo a chave "str"

print(d1)
```
Saída:
````
{'str': 'valor', 123: 'Outro valor', (1, 2, 3, 4): 'Tupla'}
{123: 'Outro valor', (1, 2, 3, 4): 'Tupla'}
```
Para checar se um valor está no dicionário, usamos:
```
d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}

print('valor' in d1.values())
```
Saída:
```
True
```
Para chaves, usamos:
```
d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}
print('str' in d1) # ou então pode usar d1.keys()
```
Saída:
```
True
```
Podemos ler quantos conjuntos (chave, valor) temno dicionário usando len(), veja:
```
d1 = {
    'str':'valor',
    123: 'Outro valor',
    (1,2,3,4): 'Tupla'
}

print(len(d1))
```
Saída:
```
3
```
Também podemos iterar sobre as **chaves** dos dicionários, usando a estrutura de repetição for, veja:
```
d1 = {
    'chave1':'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla'
}

for key in d1:
    print(key)
```
Saída:
```
chave1
chave2
chave3
```
Para iterar sobre os **valores** dos dicionário, fazemos:

```
valor
Outro valor
Tupla
```
Para ver tanto o **valor** quanto a **chave** podemos fazer assim:
```
d1 = {
    'chave1':'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla'
}

for key, value in d1.items():
    print(key, value)
```
Saída:
```
chave1 valor
chave2 Outro valor
chave3 Tupla
```
Também é possível acessa a **chave** e o **valor** de outra forma, veja:
```
d1 = {
    'chave1':'valor',
    'chave2': 'Outro valor',
    'chave3': 'Tupla'
}

for key in d1.items():
    print(key) # aqui podemos usar key[0] para acessar a chave e key[1] para acessar o valor
```
Saída:
```
('chave1', 'valor')
('chave2', 'Outro valor')
('chave3', 'Tupla')
```
Podemos fazer dicionários dentro de dicionários também, dessa forma:
```
clientes = {
    'cliente1': {
        'nome':'Denner',
        'sobrenome':'Fernandes',
    },
    'cliente2': {
        'nome':'João',
        'sobrenome':'Moreira',
    },
}

for clientes_key, clientes_value in clientes.items():
    print(f'Exibindo {clientes_key}')
    for dados_key, dados_value in clientes_value.items():
        print(f'\t{dados_key} = {dados_value}')
```
Saída:
```
Exibindo cliente1
        nome = Denner
        sobrenome = Fernandes
Exibindo cliente2
        nome = João
        sobrenome = Moreira
```
Também podemos copiar dicionários (de forma rasa) e atribuí-los a uma outra variável, veja:

```
d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1.copy()
v[1] = 'Denner'
print(v)
print(d1)
```
Saída:
```
{1: 'Denner', 2: 'b', 3: 'c'}
{1: 'a', 2: 'b', 3: 'c'}
```
Ou seja, modificamos apenas o dicionário "v"

Mas se tivermos uma lista dentro do dicionário e fizermos a cópia rasa, olha o que acontece:
```
d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Denner', 'Fernandes']}
v = d1.copy()
v[1] = 'Denner'
v['d'][0] = 'Joãozinho'

print(v['d'][0])
print(d1)
print(v)
```
Saída:
```
{1: 'a', 2: 'b', 3: 'c', 'd': ['Joãozinho', 'Fernandes']}
{1: 'Denner', 2: 'b', 3: 'c', 'd': ['Joãozinho', 'Fernandes']}```
Para copiar um dicionário de forma completa, devemos fazer assim:
```
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Denner', 'Fernandes']}
v = copy.deepcopy(d1)
v[1] = 'Denner'
v['d'][0] = 'Joãozinho'

print(v['d'][0])
print(d1)
print(v)
```
Saída:
```
{1: 'a', 2: 'b', 3: 'c', 'd': ['Denner', 'Fernandes']}
{1: 'Denner', 2: 'b', 3: 'c', 'd': ['Joãozinho', 'Fernandes']}
```
Para fazer cash em lista, ou tupla para dicioários, é muito simples. Primeiramente a lista/tupla devem ter listas que representem chave/valor no dicionáriio, deste modo:
```
lista = [
    ['c1',1],
    ['c2',2],
    ['c3',3],
]
```
Para transformar isso em um dicionário, fazemos assim:
```
lista = [
    ['c1',1],
    ['c2',2],
    ['c3',3],
]
d1 = dict(lista)
print(d1)
```
Saída:
```
{'c1': 1, 'c2': 2, 'c3': 3}
```
Também é possivel fazer como tuplas dentro de lista ou lista dentro de tupla, exemplo:
```
lista = [
    ('c1',1),
    ('c2',2),
    ('c3',3),
]
d1 = dict(lista)
print(d1)
```
Saída:
```
{'c1': 1, 'c2': 2, 'c3': 3}
```
Podemos eliminar chaves do dicioário também:
```
d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d1.pop(4)
print(d1)
```
Saída:
```
{1: 2, 2: 3}
```
popitem() elimina o a última chave, com seu valor idependente do que seja.
```
d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d1.popitem()
print(d1)
```
Saída:
```
{1: 2, 2: 3}
```
Além disso, podemos concatenar dois dicionários usando update():
```
d1 = {
    1: 2,
    2: 3,
    4: 5,
}

d2 = {
    'a':'b',
    'c':'d',
}
d1.update(d2)
print(d1)
```
Saída:
```
{1: 2, 2: 3, 4: 5, 'a': 'b', 'c': 'd'}
```
