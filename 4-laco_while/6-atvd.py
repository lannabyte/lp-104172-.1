import os
os.system('cls')

login_correto = 'Lanna'
senha_correta = '1234'

for i in range(3):
    login = input('Digite seu login: ')
    senha = input('Digite sua senha: ')

    if login == login_correto and senha == senha_correta:
        print('Bem vindo!')
        break
    else:
        print('\nLogin ou senha incorretos.')
        print('Tente novamente! \n')
        input('Precione uma tecla para continuar...')
        os.system('cls')

print('= FIM =')
