import os
os.system('cls')

# Função para exibir o logo
def logo_senai():
    print("====================")
    print("    SENAI - BAHIA")
    print("====================")

# Função para mostrar os dados
def mostrar_dados(nome, email, telefone):
    print("\n===== DADOS CADASTRADOS =====")
    print("Nome:", nome)
    print("Email:", email)
    print("Telefone:", telefone)


# Programa principal
nome = ""
email = ""
telefone = ""

while True:
    logo_senai()

    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Mostrar dados")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Digite seu nome: ")
            email = input("Digite seu email: ")
            telefone = input("Digite seu telefone: ")

            print("\nCadastro realizado!")

        case "2":
            if nome != "":
                mostrar_dados(nome, email, telefone)
            else:
                print("\nNenhum cadastro encontrado!")

        case "3":
            print("\nPrograma encerrado!")
            break

        case _:
            print("\nOpção inválida!")

    input("\nPressione ENTER para continuar...")
    os.system('cls')

