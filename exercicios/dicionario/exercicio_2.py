"""
2. Iterar sobre o dicionário: Dado o dicionário abaixo:

loja = {
    'produto1': {'nome': 'Caneta', 'preco': 1.5, 'quantidade': 100},
    'produto2': {'nome': 'Caderno', 'preco': 12.0, 'quantidade': 50},
    'produto3': {'nome': 'Lápis', 'preco': 0.75, 'quantidade': 150}
}
Desafio:
Imprima o nome de cada produto disponível na loja.
Calcule o valor total do estoque (preço x quantidade de cada produto).
Crie uma função que recebe o nome de um produto e retorna seu preço.

"""

loja = {
    'produto1': {'nome': 'Caneta', 
                 'preco': 1.5, 
                 'quantidade': 100},
    'produto2': {'nome': 'Caderno', 
                 'preco': 12.0, 
                 'quantidade': 50},
    'produto3': {'nome': 'Lápis', 
                 'preco': 0.75, 
                 'quantidade': 150}
}

def valor_produto(nome_produto: str):
    for produtos in loja:
        # Irá percorrer cada produto do dicionário e dentro de cada produto irá percorrer o nome dos dicionários
        # Caso identifique um nome igual ao que foi enviado irá pegar o valor unitário
        if loja[produtos]['nome'] == nome_produto:
            valor_unitario = loja[produtos]['preco']
            return valor_unitario

    return 'Não identificado'


# Iterando sobre os produtos e calculando o valor total
for chave, produto in loja.items():
    print(f"Nome: {produto['nome']}")
    print(f"Valor Total: {produto['preco'] * produto['quantidade']}")
    
print(valor_produto('Caneta'))