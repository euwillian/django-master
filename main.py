def envia_email(nome: str, email: str) -> str:
    return f"Email enviado para {nome} - {email}"


pessoas = [
    
    {
        'nome': 'Willian',
        'email': 'willian@gmail.com'
    },
    {
        'nome': 'Carlos',
        'email': 'Carlos@gmail.com'
    },
    {
        'nome': 'Marcel',
        'email': 'marcel@gmail.com'
    },
    {
        'nome': 'Andrey',
        'email': 'andrey@gmail.com'
    }
    
]


for i, pessoa in enumerate(pessoas):
    email_enviado = envia_email(pessoa['nome'], pessoa['email'])
    print(i, email_enviado)