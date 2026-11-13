import os
os.system('cls')

# 1. Criação das funções (uma para cada operação)
def somar(num1, num2):
    resultado = num1 + num2
    return resultado

def subtrair(num1, num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado

def dividir(num1, num2):
    # Verifica se o segundo número é zero para o programa não dar erro
    if num2 == 0:
        return "Não é possível dividir por zero!"
    else:
        resultado = num1 / num2
        return resultado


primeiro_numero = float(input("Digite o primeiro número: "))
segundo_numero = float(input("Digite o segundo número: "))

# 3. Chamando as funções 
res_soma = somar(primeiro_numero, segundo_numero)
res_sub = subtrair(primeiro_numero, segundo_numero)
res_mult = multiplicar(primeiro_numero, segundo_numero)
res_div = dividir(primeiro_numero, segundo_numero)

# 4. Mostrando tudo na tela
print("\n--- Resultados ---")
print(f"Soma: {res_soma}")
print(f"Subtração: {res_sub}")
print(f"Multiplicação: {res_mult}")
print(f"Divisão: {res_div}")