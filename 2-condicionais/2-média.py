import os
os.system('cls')

nome = (input("Digite o nome do aluno:"))
primeira_nota = float(input("Digite a primeira nota:"))
segunda_nota = float(input("Digite a segunda nota:"))
media = (primeira_nota + segunda_nota) / 2

print(f"\n nome do aluno: {nome}")

if media >= 9:
    print('Conceito A, aprovado')
elif media >= 7.5 and 9:
    print('Conceito B, aprovado')
elif media >= 6 and 7.5:
    print('Conceito C, aprovado')
elif media >= 4 and 5:
    print('Conceito D, reprovado')
else:    print('Conceito E, reprovado')





