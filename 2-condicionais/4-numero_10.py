import os
os.system('cls')

numero = int(input('Digite uma nota de 0 a 10: '))

if numero > 0 and numero <= 10:
    print(f'o seu "{numero}" esta entre 0 e 10')
else:
    print(f'o seu "{numero}" tem que estar entre 0 e 10')