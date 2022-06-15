Um iterável é um objeto que você pode iterar sobre ele, mas ele não nessesáriamente é um iterador.
Um iterador vai te dar um valor de cada vez, sempre que você precisar desse valor
Um iterador também é um iterável.
#

Existe uma forma de verificar se algo é iterável ou não em python, esse modo é o `hasattr()` que retorna True se o parametro passado for verdadeiro e False se for falso.
Exemplo:
```
lista = [0,1,2,3,4,5]
print(hasattr(lista, '__iter__'))
```
Saída:
```
True
```
####Iteráveis

Objetos iteráveis são todos aqueles que podem ser iterados por um `for`, alguns deles são:

```
listas, tuplas, dicionários, strings, sets, etc..
```

#### Não iteráveis

Objetos não iteráveis são todos aqueles que NÃO podem ser iterados pelo `for`,a lguns deles são:

```
Inteiros, etc..
```

##
Para saber se um objeto é um iterador, usamos o seguinte comando:

```
lista = [0,1,2,3,4,5]
print(hasattr(lista, '__next__'))
```
Saída:
```
False
```

Para transformar um objeto em um iterado, utilizamos o método `__iter__`, mas também podemos usar a função `iter()`, exemplo:
```
lista = [0,1,2,3,4,5]
lista = iter(lista)
print(hasattr(lista, '__next__'))
```
Agora a lista se tornou um iterador, que agora tem o método `__next__`

Saída:
```
True
```

Agora, podemos usar a função `next()` para printar cada elemento da lista separadamente, como por exemplo:

```
lista = [0,1,2,3,4,5]
lista = iter(lista)

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

print(hasattr(lista, '__next__'))
```
Saída:
```
0
1
2
3
4
5
True
```
Resumindo: Criamos um `for` sem criar o `for`, e podemos imprimir o elemento que desejamos da lista

#

Existe uma forma de retornar um elemento de cara vez, sem que todos eles já estejam emuma lista, esse método chama-se `yield`
Veja um exemplo sem o `yield`:

```
imort time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r
   
g = gera()
for v in g:
    print(v)
```
A saída é:
```
0
1
2
3
4
5
6
7
8
9
10
... (Até o 99)
```

Com o método `yield`, ele irá retornar `n` toda hora que `n` se tornar outro valor:
Obs: Não haverá diferença entra assaídas, para ver difereãnça copie e execute ambos os códigos

```
import time

def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)

g = gera()

for v in g:
    print(v)
```
No momento em que o `yield` é adicionado, a função se torna um **Gerador**. 
Obs: Um gerador é iterável, por isso podemos usar o `for`.
Saída:
```
1
2
3
4
5
6
7
8
9
10
... (Até o 99)
```
Para provar que a função é um gerador, podemos dar um print em `g`:

```
print(g)
```
Saída:
```
<generator object gera at 0x004FB338>
```

Outro exemplo:
```
def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gera()
print(next(g))
```
Saída:
```
Valor 1
```
Se utilizarmos outros `print(next(g))`, ele irá mostrar `Valor 2` na tela:
```
def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gera()
print(next(g))
print(next(g))
```
Saída:
```
Valor 1
Valor 2
```
Se utilizarmos outro `print(next(g))` a saída será:
```
Valor 1
Valor 2
Valor 3
```
E assim conforme a quantidade de `yield` na função. Mas lembrando, que a melhor maniera de fazer isso, é com o `for`.

#
Podemos criar um gerador, da seguinte forma:
```
lista = [x for x in range(1000)]
print(type(lista))
lista = (x for x in range(1000))
print(type(lista))
```
Saída:
```
<class 'list'>
<class 'generator'>
```
Ou seja, de uma lista usando list comprehensions, foi para um gerador (que aparenta ser uma tupla com list comprehensions, por isso não confunda) para um gerador.

#
Podemos verificar quanto de memória uma lista e um gerador consomem na memória do computador:

```
l1 = [x for x in range(100000)]
l2 = (x for x in range(100000))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2))
```  
Saída:
```
412228
56
```
Veja a diferença entre uma lista e um gerador: A lista consome 412228 bytes na memória, enquanto o gerador, só 56. 
Se alterarmos de 100000 para 1000000, a lista aumentaria (muito) o tamanho na memória, mas o gerador permaneceria igual.