"""
list comprehension python

[expressão for i in list condicional]
Leia-se: aplique a expressão para cada item da lista que atende a condicional

"""
#1 - forma comum de realizar
numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []

for n in numeros:
    numeros_dobrados.append(n * 2)

print(numeros_dobrados)

#1 Usando comprehension list
numeros_dobrados_comprehension = [n * 2 for n in numeros]
print(numeros_dobrados_comprehension)


# 2
nomes = ["João", "Carlos", "Marcos", "José", "Cleiton"]

nomes_maisculo = [nome.upper() for nome in nomes]
print(nomes_maisculo)


# 3
nomes_com_letra_j = [nome.upper() for nome in nomes if nome.startswith("J")] 
# se o nome iniciar com a letra J então adicione ele na lista
print(nomes_com_letra_j)