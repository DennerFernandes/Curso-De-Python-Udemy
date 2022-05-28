def fizz_buzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return 'Fizz Buzz'
    if numero % 3 == 0:
        return 'Fizz'
    if numero % 5 == 0:
        return 'Buzz'
    return numero


from random import randint

for i in range(100):
    aleatorio = randint(0, 100)
    print(fizz_buzz(aleatorio))
