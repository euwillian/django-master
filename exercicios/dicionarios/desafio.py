"""
Jogo de Palavras: Use um dicionário para criar um jogo de palavras onde o usuário 
digita uma palavra e o programa retorna o significado correspondente. Por exemplo:

palavras = {
    'Python': 'Uma linguagem de programação.',
    'Dicionário': 'Uma coleção de pares chave-valor.'
}
Crie um menu para adicionar palavras e significados ao dicionário.
Permita ao usuário buscar o significado de uma palavra."""

palavras = {
    'python': 'Uma linguagem de programação.',
    'dicionário': 'Uma coleção de pares chave-valor.'
}


def incluir_nova_palavra(palavra: str, significado: str) -> str:
    if palavra not in palavras:
        palavras[palavra] = significado
        return "Registrado com Sucesso!"
    else:
        palavras[palavra] = significado
        return "Significado atualizado!"
    
    
def buscar_palavra(palavra: str) -> str:
    significado = palavras.get(palavra, "Palavra inexistente!")
    return significado


usuario_continuar = True

while usuario_continuar:
        
    continuar = int(input(
            "Escolha uma opção:\n"
            "1 - Inserir nova palavra/significado\n"
            "2 - Buscar uma palavra\n"
            "3 - Sair\n"))
    
    if continuar == 1:
        palavra = input("Informe uma nova palavra: ").lower()
        significado = input("Informe seu significado: ")
        print(incluir_nova_palavra(palavra=palavra, significado=significado))
    elif continuar == 2:
        palavra = input("Informe a palavra que deseja buscar: ").lower()
        print(buscar_palavra(palavra=palavra))
    else:
        usuario_continuar = False
