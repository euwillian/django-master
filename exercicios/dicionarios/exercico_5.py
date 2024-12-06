"""Nível 5: Aplicação Prática
Gerenciador de Tarefas: Crie um sistema de gerenciamento de tarefas usando dicionários. 
Cada tarefa deve ter:

ID único
Título
Descrição
Status (pendente ou concluído)
Data de criação
Desafio:

Adicione novas tarefas ao sistema.
Marque uma tarefa como concluída.
Liste todas as tarefas pendentes.
Remova uma tarefa concluída pelo ID."""

gerenciador_tarefas = {}

def adicionar_tarefa(id: int, titulo: str, descricao: str, status: str, data_criacao: str) -> str:
    """Cadastrar novas tarefas"""
    if status == "pendente" or status == "concluido":
        if id not in gerenciador_tarefas:
            gerenciador_tarefas[id] = {"titulo": titulo,
                                    "descricao": descricao,
                                    "status": status,
                                    "data_criacao": data_criacao}
            return "Tarefa cadastrada!"
        return "Id já cadastrado!"
    return "status inválido!"

def concluir_tarefa(id: int) -> str:
    """Concluir tarefas pendentes"""
    if id in gerenciador_tarefas:
        gerenciador_tarefas[id]["status"] = "concluido"
        return f"tarefa com {id} foi marcado como concluído! "


def listar_pendencias() -> list:
    """Retorna todas tarefas com status pendente"""
    tarefas_pendetes = []
    for chave, tarefa in gerenciador_tarefas.items():
        if tarefa["status"] == "pendente":
            tarefas_pendetes.append(tarefa["titulo"])

    
    if len(tarefas_pendetes) > 0:
        return tarefas_pendetes
    else:
        return "Não existem tarefas pendentes"
        

def remover_tarefa_por_id(id: int) -> str:
    """Remover tarefas por id"""
    if id in gerenciador_tarefas:
        tarefa = gerenciador_tarefas[id]["titulo"]
        gerenciador_tarefas.pop(id)
        return f"Foi removida a tarefa de id {id} - {tarefa}!"
    return "Id inexistente ou já removido!"


adicionar_tarefa(1, "Programar", "Programar diariamente", "pendente", "06/12/2024")
adicionar_tarefa(2, "Trabalhar", "Trabalhar diariamente", "pendente", "07/12/2024")
concluir_tarefa(2)
listar_pendencias()
print(gerenciador_tarefas)
print(remover_tarefa_por_id(1))

