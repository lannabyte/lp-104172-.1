import os
os.system('cls')

soma = 0
pares = 0
impares = 0
soma_pares = 0

numero = int(input("Digite um número: "))

while numero != 0:

    soma = soma + numero

    if numero % 2 == 0:
        pares = pares + 1
        soma_pares = soma_pares + numero
    else:
        impares = impares + 1

    numero = int(input("Digite um número: "))

print("Pares:", pares)
print("Ímpares:", impares)

if pares > 0:
    print("Média dos pares:", soma_pares / pares)

print("Média geral:", soma / (pares + impares))