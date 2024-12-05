"""Nível 4: Manipulação Complexa
Banco de Dados de Livros: Crie um dicionário que simule um banco de dados de livros. 
Cada livro deve ter:

Título
Autor
Ano de publicação
Gênero
Quantidade disponível
Desafio:

Crie uma função para adicionar novos livros.
Crie uma função para emprestar um livro, reduzindo sua quantidade disponível.
Crie uma função para listar todos os livros de um determinado gênero.
Faça uma busca pelo título do livro e retorne todas as informações sobre ele."""

livros = {}

def adicionar_livros(titulo: str, autor: str, ano_publicacao: int, genero: str, quantidade_disponivel: int) -> None:
    """Adicionar livros"""
    livros[titulo] = {"autor": autor,
                        "ano_publicacao": ano_publicacao,
                        "genero": genero,
                        "quantidade_disponivel": quantidade_disponivel}


def emprestar_livro(titulo_do_livro: str) -> str:
    """Emprestar livros"""
    if titulo_do_livro in livros:
        if livros[titulo_do_livro]["quantidade_disponivel"] > 0:
            livros[titulo_do_livro]["quantidade_disponivel"] -= 1
            return "Emprestimo realizado com sucesso"
        return "Livro indisponível."
    return "Este título não existe."
    

def livros_por_genero(genero: str) -> list:
    """Funcao para retornar os livros por genero"""
    titulos_encontrados = []
    for livro in livros:
        if livros[livro]["genero"] == genero:
            titulos_encontrados.append(livro)
            
    return titulos_encontrados


def buscar_por_titulo(titulo_do_livro: str) -> str:
    """Busca os livros por titulo"""
    if titulo_do_livro in livros:
        autor = livros[titulo_do_livro]["autor"]
        ano   = livros[titulo_do_livro]["ano_publicacao"]
        genero= livros[titulo_do_livro]["genero"]
        qntd  = livros[titulo_do_livro]["quantidade_disponivel"]
        return f"{autor}, {ano}, {genero}, {qntd}"
    else:
        return "Inexistente"


adicionar_livros(titulo="Arca", autor="Enri", ano_publicacao=2012, genero="Biblico", quantidade_disponivel=4)
adicionar_livros(titulo="Noé", autor="Enri", ano_publicacao=2013, genero="Biblico", quantidade_disponivel=500)
adicionar_livros(titulo="Moises", autor="Enri", ano_publicacao=1999, genero="Biblico", quantidade_disponivel=300)
adicionar_livros(titulo="Python", autor="Adm", ano_publicacao=2024, genero="Técnico", quantidade_disponivel=100)


print(livros_por_genero(genero="Biblico"))
print(buscar_por_titulo(titulo_do_livro="Python"))
