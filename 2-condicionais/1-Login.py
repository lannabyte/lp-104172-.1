import os
os.system('cls')

login = ('Judas').lower()
senha =  ('x9morrecedo')

login1 = input('Digite seu login: ')
senha2 = input('Digite sua senha: ')

if login == login1 and senha == senha2:
    print('Bem-vindo!')
else:
    print('login ou senha inválidos')


