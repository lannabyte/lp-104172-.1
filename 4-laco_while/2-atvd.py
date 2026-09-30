import os 
os.system('cls')

while True:
    nota = int(input("Digite uma nota entre 0 e 10:"))
    if nota < 1 or nota > 10:
        print('Nota inválida, tente novamente!')
    else:
        print('A nOTA está entre 1 e 10.')
        print(F'Nota: {nota} ')
        break # Serve para parar o laço de repetição.
    
    print('= FIM =')
