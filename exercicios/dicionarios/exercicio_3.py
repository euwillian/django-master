"""
Nível 3: Dicionários aninhados
Cadastro de Pessoas: Implemente um programa que permita cadastrar informações sobre várias pessoas. Cada pessoa deve ter:

Nome
Idade
Profissão
Lista de hobbies
Desafio:

Permita adicionar novas pessoas ao dicionário.
Permita atualizar informações de uma pessoa específica.
Permita buscar uma pessoa pelo nome e listar todas as suas informações.

"""

dicionario_de_pessoas = {}

def incluir_pessoas(nome: str, idade: int, profissao: str, hobbies: list) -> None:
    dicionario_de_pessoas[nome] = {'idade': idade,
                                   'profissao': profissao,
                                   'hobbies': hobbies}
    

def atualizar_idade(nome: str, nova_idade: int) -> str:
    if nome in dicionario_de_pessoas:
        dicionario_de_pessoas[nome]['idade'] = nova_idade
        return "Idade atualizada com sucesso"
    return "Pessoa não encontrada"    


def buscar_dados_pessoa(nome: str) -> dict:
    return dicionario_de_pessoas.get(nome, "Pessoa não encontrada")


# Inclusão de dados via função
incluir_pessoas("Willian", 29, 'Dev', ["programar", "estudar"])
incluir_pessoas("Giovana", 29, 'CSM', ["Comercial", "Academia"])
incluir_pessoas("Priscila", 32, 'RH', ["Atendimento", "Dançar"])
incluir_pessoas("Claudete", 50, 'Do lar', ["Netflix", "Cozinhar"])

# Atualizar exemplo
print(atualizar_idade("Willian", 30))

# Buscar uma pessoa especifica
print(buscar_dados_pessoa('Willian'))