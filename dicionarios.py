"""
Dicionários em Python


"""
meu_dicionario = {'nome': 'Willian', "idade": 29}

# Acessar valores 1
print(meu_dicionario['nome'])

# Acessar valores 2
print(meu_dicionario.get('nome', 'Chave não existente'))

# Conclusão: A escolha depende do contexto. No geral, o método .get() é mais seguro em casos onde há incerteza sobre a presença de chaves.


# Remover valores
meu_dicionario.pop('idade')

# Listar todas as chaves do dicionário
meu_dicionario.keys()

# Listas os valores sem as chaves do dicionário
meu_dicionario.values()

# Limpa todo o dicionário
meu_dicionario.clear()

# Dicionário Complexo

pessoa = {
    'nome': 'Willian',
    'idade': 29,
    'interesses': ['programação', 'Python', 'jogos'],
    'pet': {'nome': 'Kiara',
            'idade': 8,
            'raca': 'sem raça',
            'brinquedos': {'nome': 'Bolinha',
                           'qntd': 10
        }
    }
}

# Adicionar uma nova chave/ valor ao dicionário já criado
pessoa['trabalho'] = 'novo'

# Adicionei um novo item dentro da lista de uma lista
pessoa.get('pet')['cor'] = 'branco'

print(pessoa)

print(pessoa.get('pet', 'não definido').get('brinquedos', 'nao definido').get('nome', 'nao definido'))