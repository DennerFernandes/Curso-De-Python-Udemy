List comprehensions (em português compreensão de listas), basicamente são iterações que fazemos apara cada elemento de uma determinada lista, que o atribuimos a outra lista, exemplo:
```
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel for variavel in l1]

print(l2)
```
Podemos manipular a **variavel** que está na lista 2, por exemplo, podemos multiplicar todos os elementos da l1 por 2 e os atribuir a l2.
```
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [variavel*2 for variavel in l1]
print(l2)
```
Saída:
```
[2, 4, 6, 8, 10, 12, 14, 16, 18]
```
Outro exemplo seria:
```
l1 = [1,2,3,4,5,6,7,8,9]
l2 = [(variavel,variavel2) for variavel in l1 for variavel2 in range(3)]
print(l2)
```
Saída:
```
[(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2), (6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2), (9, 0), (9, 1), (9, 2)]
```
Outro exemplo:
```
l1 = ['Luiz', 'Mauro', 'Maria']
l2 = [v.replace('a', '@').upper() for v in l1]
print(l2)
```
Saída:
```
['LUIZ', 'M@URO', 'M@RI@']
```
Outro exemplo:
```
l1 = list(range(0,100))
l2 = [v for v in l1 if v % 2 == 0]

print(l2)
```
Saída:
```
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
```