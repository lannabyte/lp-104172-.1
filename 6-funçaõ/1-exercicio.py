import os
os.system('cls')

def logo_senai():
    print("===================")
    print("  SENAI - BAHIA    ")
    print("===================")

def mostrar_dados(nome, email, telefone):

    print("\n===== DADOS CADASTRADOS =====")
    print("Nome:", nome)
    print("Email:", email)
    print("Telefone:", telefone)

logo_senai()

nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone: ")
mostrar_dados(nome, email, telefone)


