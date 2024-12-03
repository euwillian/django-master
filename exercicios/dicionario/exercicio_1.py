"""
1. Criar e acessar itens: Crie um dicionário que represente um aluno, com as seguintes informações:

Nome
Idade
Lista de matérias que ele estuda
Uma nota para cada matéria (em outro dicionário)
Desafio:

Acesse e imprima o nome do aluno.
Adicione uma nova matéria com uma nota.
Atualize a nota de uma matéria já existente.

"""

aluno = {'nome': 'Willian Souza dos Santos',
         'idade': 29,
         'materias': ['portugues', 'matematica', 'fisica', 'quimica'],
         'notas':{'portugues': 8, 
                  'matematica': 10, 
                  'fisica': 9, 
                  'quimica': 8}
         }

print(aluno.get('nome', 'inexistente'))
aluno['notas']['ingles'] = 8
aluno['notas']['portugues'] = 7

print(aluno)