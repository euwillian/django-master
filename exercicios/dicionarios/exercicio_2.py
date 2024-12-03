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

# Função para buscar o valor de um produto pelo nome
def valor_produto(nome_produto: str):
    for chave, produto in loja.items():
        if produto['nome'] == nome_produto:
            return produto['preco']
    return None  # Mais semântico que 'Não identificado'


for chave, produto in loja.items():
    print(f"Nome: {produto['nome']}")
    print(f"Valor Total: {produto['preco'] * produto['quantidade']}")
    
print(valor_produto('Caneta'))