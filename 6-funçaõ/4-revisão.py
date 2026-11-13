import os
os.system('cls')

# funçaõ sem retorno e sem parametros
def logo_senai():
    os.system('cls')
    print('===============')
    print(' SENAI ')
    print('===============')

# função sem retorno e com parametros
def mostrar_dados(nome, idade):
    print(f'{nome} tem {idade} anos.')

# função sem retorno e sem parametros
logo_senai()
print('\n= SOLICITANDO DADOS =')
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

logo_senai()
print('\n= EXIBINDO DADOS =')

# função sem retorno e com parâmetros
mostrar_dados(nome, idade)