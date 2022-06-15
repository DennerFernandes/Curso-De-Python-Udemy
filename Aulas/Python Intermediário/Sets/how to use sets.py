# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da equerda)
# symmetric_difference ^(Elementos que estão nos dois sets, mas não em ambom simultaneamente)

"""
Criando um set
"""

# s1 = {}

#  Ou

# s1 = set()

"""
Adicionando elementos no set
"""

# s1 = {1,2,3,4,5}
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.add(4)
# s1.add(5)

"""
Removendo o valor de um set
"""
# s1 = set()
# s1.add(1)
# s1.add(2)
# s1.add(3)
# s1.add(4)
# s1.add(5)

# s1.discard(2)

# print(s1)
"""
Atualizando o set
"""

# s1 = set()
# s1.update('Python')
# print(s1)

"""
Removendo elementos duplicados de uma lista
"""
# l1 = [1,2,1,1,3,4,5,6,6,6,6,6,7,8,9,'Denner', 'Denner']
# l1 = set(l1)
# l1 = list(l1)
# print(l1)

"""
Unindo sets
"""

# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 | s2
# print(s3)

"""
Encontrando a igualdade de dois sets
"""

# s1 = {1,2,3,4,5}
# s2 = {1,2,3,4,5,6}
# s3 = s1 & s2
# print(s3)


"""
Encontrando a diferença entre dois sets
"""
s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s2 ^ s1
print(s3)


