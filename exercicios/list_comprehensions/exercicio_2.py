"""
Exercício 2: Intermediário
Dada a lista abaixo, use list comprehension para criar uma nova lista contendo apenas os números pares.
numeros = [3, 7, 2, 8, 5, 10, 4, 11, 14]
"""

numeros = [3, 7, 2, 8, 5, 10, 4, 11, 14]
numeros_pares = [num for num in numeros if num % 2 == 0]
print(numeros_pares)