import os
os.system('cls')

#LISTA DE PRODUTOS
lista_produtos = []

while True:
    #limpa o terminal
    os.system('cls')
#menu do progama
    print('''
=== MERCADINHO DENDEZEIROS ===
1 - Cadastrar produtos
2 - Listar produtos
3 - Sair
    ''')
    
    opcao = int(input('Digite a opção desejada: '))
    
    match opcao:
        case 1:
            print('\n=== CADASTRAR UM PRODUTO ===')
            # strip() retira os espaços vazios no final.
            # upper() todas as letras maiusculas.
            nome = input('Digite o nome do produto: ').strip().upper()

            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
                print(f'{nome} já está cadastrado.')
            else:
                # .append() adiciona um elemento no final da lista.
                lista_produtos.append(nome)
                print(f'\nProduto {nome} cadastrado com sucesso!')
            input('Pressione uma tecla para continuar...')
        case 2:
            print('\n== PRODUTOS NO ESTOQUE ==')
            if len(lista_produtos) == 0:
                print('O estoque está vazio.')
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f'{i+1}. {produto}')
                
                # len(lista_produtos) mostra a quantidade de produtos na lista.
                print(f'Total de produtos: {len(lista_produtos)}')
            input('\nPressione uma tecla para continuar...')
            
        case 0:
            print('Fim do programa.')
            input('Pressione uma tecla para continuar...')
            
        case _:
            print('Opção inválida!')
            input('Pressione uma tecla para continuar...')


