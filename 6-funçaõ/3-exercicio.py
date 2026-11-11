import os
os.system('cls')

def tabuada(numero):
    print("\n===== TABUADA =====")
    
    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)

print("=== CALCULADORA DE TABUADA ===")

numero = int(input("Digite um número: "))

tabuada(numero)
