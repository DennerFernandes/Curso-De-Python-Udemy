# variavel = 'valor'
#
# def func():
#     print(variavel)
#
# def func2():
#     global variavel
#     variavel = 'Outro valor'
#     print(variavel)
#
# func()
# func2()
#
# print(variavel)

# ---------------------------------------

def func():
    outra_variavel = 'Denner'
    return outra_variavel
def func2(arg):
    print(arg)

var = func()
func2(var)
