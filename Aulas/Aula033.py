"""
Aula 33 - Manipulando Strings

* String indices
* Fatiamneto de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem seer usadas diretamente em cada tipo

Você pode conferir tudo isso em:
  https://docs.python.org/3/libary/stdtypes.html
  https://docs.python.org/3/libary/functions.html

"""

# indices positivos   [012345678]
texto               = 'Python s2'
# indices negativos  -[987654321]
print(texto[2])

##################################

url = 'www.google.com.br/'
print(url[:-1])

##################################

nova_string = texto[:-1]
print(nova_string)

############Passos###############

nova_string = texto[0::3]
print(nova_string)