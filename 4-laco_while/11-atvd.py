import os
os.system('cls')

soma_notas = 0
contador = 0

while True:
    nota = float(input("Digite uma nota: "))
    soma_notas += nota
    
    contador += 1
    
    resposta = input("Deseja inserir mais uma nota? (S/N): ").upper()
    
    if resposta == "N":
        break

if contador > 0:
    media = soma_notas / contador
    print(f"\nTotal de notas inseridas: {contador}")
    print(f"A média aritmética das notas é: {media:.2f}")
