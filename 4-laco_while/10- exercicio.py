import os
os.system('cls')

print("===== CADASTRO =====")

login_cadastrado = input("Crie seu login: ")
senha_cadastrada = input("Crie sua senha: ")

input("\nCadastro realizado! Pressione ENTER para continuar...")

os.system("cls")

print("===== LOGIN =====")

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == login_cadastrado and senha == senha_cadastrada:
        print("\nBem-vindo!")
        break
    else:
        print("\nLogin ou senha incorretos!")
        print("Tente novamente.\n")
        