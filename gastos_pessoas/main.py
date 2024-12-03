import json

def menu():
    opcao = int(input(
                    "1. Registrar um novo gasto\n"
                    "2. Listar todos os gastos\n"
                    "3. Filtrar gastos por categoria\n"
                    "4. Exibir total de gastos por mês\n"
                    "5. Editar um gasto\n"
                    "6. Excluir um gasto\n"
                    "7. Sair\n"
                    "Escolha uma opção: "
                ))

    match opcao:
        case 1:
            print("\n\n")
            
            print("Para registrar um novo gasto informe: ")
            descricao_gasto = input("Descrição: ")
            valor_gasto = float(input("Valor: "))
            categoria = input("Categoria: ")
            data = input("Data: ")
            
            registrar_gasto = novo_gasto(descricao=descricao_gasto, valor=valor_gasto, categoria=categoria, data=data)
            print(registrar_gasto)
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass
        case 7:
            print("Programa encerrado!")
        case _:
            print("Opção inválida!")


def novo_gasto(descricao: str, valor: float, categoria: str, data: datetime) -> str:
    dados = {
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": data
    }
    
    with open("dados.json", "w") as arquivo:
        json.dump(dados, arquivo)
        
    arquivo.close()
    
    return "Gasto registrado com sucesso!"


def listar_gastos():
    pass


def filtrar_gastos(categoria: str):
    pass


def gastos_mes():
    pass


def editar_gasto():
    pass


def excluir_gasto():
    pass


menu()