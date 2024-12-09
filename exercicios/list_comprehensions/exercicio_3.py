"""
Exercício 3: Avançado
Dada a lista de nomes abaixo, use list comprehension para criar uma 
nova lista contendo apenas os nomes que começam com a letra "A" 
(maiúscula ou minúscula), convertidos para maiúsculas.

Lista fornecida:
nomes = ["Ana", "Bruno", "alice", "André", "Carla", "amanda"]

"""
nomes = ["Ana", "Bruno", "alice", "André", "Carla", "amanda"]

nomes_iniciados_por_a = [nome.upper() for nome in nomes if nome.upper().startswith("A")]
print(nomes_iniciados_por_a)


