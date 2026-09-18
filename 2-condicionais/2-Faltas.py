import os
os.system('cls')

nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))
nota3 = float(input("Digite sua nota: "))
faltas = int(input("Digite suas faltas: "))

soma = nota1 + nota2 + nota3
media = soma / 3

if media >= 7 and faltas <=40:
    print('parabens aluno aprovado')
else:
    print('aluno reprovado')



