string = '012345678901234567890123456789012345678901234567890123456789'
lista = [string[:10] for i in range(1,len(string[::8]) - 1)]

print('.'.join(lista))
