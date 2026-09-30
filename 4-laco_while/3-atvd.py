import os
os.system('cls')

soma = 0
QUANTIDADE_NOTAS = 2

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota = float(input(f'Digite a {i+1}ª nota entre 8 e 10: '))
        if nota >= 8 and nota <= 10:
            soma = soma + nota
            break  # Serve para parar o laço de repetição.
        else:
            print()  # Pular uma linha
            print('Nota inválida, tente novamente!')

media = soma / QUANTIDADE_NOTAS

print(f'Média: {media}')
print('= FIM =')

    