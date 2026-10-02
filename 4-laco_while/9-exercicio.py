import os
os.system('cls')

while True:
    print('1 - Base - R$ 35,00')
    print('2 - Corretivo - R$ 25,00')
    print('3 - Blush - R$ 20,00')
    print('4 - Batom - R$ 15,00')
    print('5 - Máscara de cílios - R$ 22,00')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('Opção escolhida: Base - R$ 35,00')
        break

    if opcao == 2:
        print('Opção escolhida: Corretivo - R$ 25,00')
        break

    if opcao == 3:
        print('Opção escolhida: Blush - R$ 20,00')
        break

    if opcao == 4:
        print('Opção escolhida: Batom - R$ 15,00')
        break

    if opcao == 5:
        print('Opção escolhida: Máscara de cílios - R$ 22,00')
        break

    print('Opção inválida!')
