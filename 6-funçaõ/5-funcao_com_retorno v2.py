import os
os.system('cls')

def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2 / 2
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: ')) 
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parametors e
# inserindo o retorno na variavel soma.
media = calcular_notas(nota1, nota2)

print('\n= EXIBINDO NOTAS =')
print(f'Média: {media} ')

