import os 
os.system('cls')

def verificar_pares_ou_impares(numero):
    if numero % 2 == 0:
        print(f" o numero {numero} é par")
    else:
        print(f" o numero {numero} é impar")

valor = int(input("Digite um número: "))
verificar_pares_ou_impares(valor)

