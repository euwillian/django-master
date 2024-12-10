"""
Variáveis de ambiente
    
powershell:

$env:USUARIO_API = 'valor'
$env:SENHA_API = 'valor'    
"""
import api
import os

usuario = os.environ.get('USUARIO_API')
senha = os.environ.get('SENHA_API')

print(usuario, senha)
login = api.logar(usuario, senha)
print(login)