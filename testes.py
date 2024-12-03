import random

# Lista base de frutas
frutas_base = ["maçã", "banana", "laranja", "uva", "morango", "kiwi", "manga", "abacate", "cereja", "pera"]

# Criar lista de frutas com 10.000 itens
lista_frutas = [random.choice(frutas_base) for _ in range(10000)]

# A lista 'lista_frutas' agora contém 10.000 itens
print(lista_frutas)

r = lista_frutas
cont = 0

print(r.count('banana'))

for i, fruta in enumerate(r):
    if fruta == 'banana':
        del r[i]
        cont += 1
    
print(f"tem ainda: {r.count('banana')} - contador: {cont} ")