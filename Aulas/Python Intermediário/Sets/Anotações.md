Sets só suportam elementos imutáveis, ou seja, só aceitam: números, strings ou tuplas.
Além disso, não é possível acessar os indices do set.

Existem duas maneiras de criar sets, tanto com chaves **{ }** como usando **set( )**.
Usando chaves fica confuso, pois é muito parecido com um dicionário, então usaremos set().
```
s1 = {}
s2 = set()
```
Para colocar valores nos sets, é muito similar as listas, ou as tuplas, veja:
```
s1 = {1,2,3,4,5}
```
Já para adicionar usando a função **set( )**, devemos usar o método add. (Também funciona criando sets com chaves):
```
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)
```
Para remover um valor de um set, usamos dicard(), deste modo:
```
s1 = set()
s1.add(1)
s1.add(2)
s1.add(3)
s1.add(4)
s1.add(5)

s1.discard(2)

```
Saída:
```
{1, 3, 4, 5}
```
Para atualizarmos os set, uzamos a função **update( )**:
```
s1 = set()
s1.update('Python')

print(s1)
```
Obs 1: a função **update( )** só recebe valores ***iteráveis*** e itera sobre cada um deles,ou seja, só recebe listas, tuplas, strings, outros sets, entre outros. Por isso a saída é:
```
{'t', 'y', 'n', 'P', 'o', 'h'}
```
Obs 2: Sets não retornam o valores ordenado,por isso sempre que executar o programa, verá os valores fora de ordem.

Sets não aceitam elementos duplicados, ou seja, são perfeitos para retiralos de uma lista, ou tupla por exemplo.
```
l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9,'Denner', 'Denner']
l1 = set(l1) # Fazendo cast 
l1 = list(l1)
print(l1)
```
Saída:
```
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'Denner']
```
Vemos que o set removeu completamente os itens duplicados

Podemos unir dois sets usando a função **union** ou **|**
```
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2
print(s3)
```
Saída:
```
{1, 2, 3, 4, 5, 6}
```
Observamos novamente que o set não aceitou os itens duplicados, então ele uniu somente o **6** 

Podemos achar a interseção de dois sets, ou seja, todos os elementos presentes em ambos os sets.Podemos utilizar tanto  **intersection( )** quanto **&** para fazer isso
```
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 & s2
print(s3)
```
Saída:
```
{1,2,3,4,5}
```
Para enocontrar a diferença entre dois sets usamos **difference( )** ou **-**
```
s1 = {1,2,3,4,5}
s2 = {1,2,3,4,5,6}
s3 = s1 - s2
print(s3)
```
Saída:
```
{6}
```
Obs: nesse caso a ordem importa


Para encontrar a diferença simétrica entre doi sets, usamos **symmetric_difference( )** ou **^**
```
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s2 ^ s1
print(s3)
```
Saída:
```
{6, 7}
```
