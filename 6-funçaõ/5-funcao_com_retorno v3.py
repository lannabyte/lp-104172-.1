import os
os.system('cls')

def calcular_notas(nota1, nota2):
    resultado = nota1 + nota2 / 2
    return resultado

def verificar_resultados(media):
    if media >=7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado

print('= SOLICITANDO NOTAS =')
nota1 = float(input('Digite a primeira nota: ')) 
nota2 = float(input('Digite a segunda nota: '))

# Usando a função com parametors e
# inserindo o retorno na variavel soma.
media = calcular_notas(nota1, nota2)
situacao = verificar_resultados(media)

print('\n= EXIBINDO NOTAS =')
print(f'Média: {media} ')
print(f'Resultado: {situacao}')

if media >=7.0:
    print("\nAluno aprovado")
    print("\nAluno reprovado")


