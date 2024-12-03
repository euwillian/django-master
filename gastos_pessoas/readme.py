"""
gastos_pessoais.py


Projeto: Sistema de Controle de Gastos Pessoais

Descrição Geral:
Desenvolver um sistema simples para registrar e monitorar gastos pessoais. O sistema será executado no terminal e armazenará os dados localmente em um arquivo.


Funcionalidades:
Requisitos Funcionais:
Cadastro de Gastos:

Permitir que o usuário registre um gasto com:
- Descrição.
- Valor.
- Categoria (ex.: Alimentação, Transporte, Lazer).
- Data (usar data atual por padrão, mas permitir edição).

Consulta de Gastos:

- listar todos os gastos cadastrados.
- Filtrar gastos por categoria.
- Mostrar o total de gastos por mês.
- Edição e Exclusão de Gastos:

Usuário pode corrigir um gasto já registrado.
Permitir excluir um gasto.

Armazenamento:

Os dados devem ser salvos em um arquivo JSON para persistência.

Requisitos Não Funcionais:
Usabilidade:

- Sistema deve ser simples, com menus interativos no terminal.
- Feedback amigável ao usuário (ex.: "Gasto registrado com sucesso!").

Segurança:

- Validar entrada de dados (ex.: valores numéricos para o campo de valor).
- Impedir ações inválidas, como excluir um gasto inexistente.


Tecnologias Envolvidas:
- Linguagem: Python.
- Armazenamento: Arquivo JSON.

Bibliotecas:
- json para manipulação dos dados.
- datetime para lidar com datas.


Prazos:
7 dias para conclusão.

Sugestão de etapas:
- Dia 1-2: Estruturar o cadastro de gastos e salvar no arquivo JSON.
- Dia 3-4: Implementar a listagem e os filtros.
- Dia 5: Adicionar a edição e exclusão.
- Dia 6: Testar e corrigir bugs.
- Dia 7: Melhorar a interface de usuário no terminal.

Critérios de Aceitação:
- Todos os gastos são registrados e armazenados corretamente.
- Listagem, filtro, edição e exclusão funcionam como esperado.
- Interface clara e fácil de usar.



https://pythonacademy.com.br/blog/como-manipular-json-no-python
https://pydetodos.com/manipular-arquivos-json-com-python/
"""

