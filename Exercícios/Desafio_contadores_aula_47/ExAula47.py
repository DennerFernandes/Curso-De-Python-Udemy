"""
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
progressivo = list(range(0, 9))
regressivo = list(range(10, 1, -1))
contador = 0
while contador < len(progressivo):
    print(f'{progressivo[contador]} {regressivo[contador]}')
    contador += 1


# for progressivo, regressivo in enumerate(range(10, 1, -1)):
