import os

lista_produtos = []
while True:
    os.system('cls')
    # Menu do programa.
    print('''
    === MERCADINHO DENDEZEIROS ===
    1 - Cadastrar produto
    2 - Listar produtos
    3 - Atualizar produto
    4 - Remover produto
    5 - Buscar produto
    0 - Sair
    ''')
    opcao = input('Escolha uma opção: ')
    match opcao:
        case '1':
            # CREATE (CRIAR)
            print('\n== CADASTRAR UM PRODUTO ==')
            nome = input('Nome do produto: ').strip().upper()
            if nome == '':
                print('O nome não pode ficar vazio.')
            elif nome in lista_produtos:
                print(f'{nome} já está cadastrado.')
            else:
                lista_produtos.append(nome)
                print('Produto cadastrado com sucesso!')
            input('\nPressione uma tecla para continuar...')
        case '2':
            # READ (LER / CONSULTAR / BUSCAR)
            print('\n== LISTA DOS PRODUTOS ==')
            if len(lista_produtos) == 0:
                print('O estoque está vazio')
            else:
                for i, produto in enumerate(lista_produtos):
                    print(f"{i+1}º Produto: {produto}")
                print(f'Total de produtos: {len(lista_produtos)}')
            input('\nPressione uma tecla para continuar...')
        case '3':
            # UPDATE (ATUALIZAR)
            print('== ATUALIZAR PRODUTO ==')
            nome = input('Qual o produto deseja atualizar? ').strip().upper()
            if nome in lista_produtos:
                posicao = lista_produtos.index(nome)
                novo = input('Novo nome: ').strip().upper()
                lista_produtos[posicao] = novo
                print('Produto alterado com sucesso!')
            else:
                print('Produto não encontrado.')
            input('\nPressione uma tecla para continuar...')
        case '4':
            # REMOVE/DELETE (REMOVER / DELETAR)
            print('== REMOVER PRODUTO ==')
            nome = input('Qual produto deseja remover? ').strip().upper()
            if nome in lista_produtos:
                lista_produtos.remove(nome)
                print('Produto removido com sucesso!')
            else:
                print('Produto não encontrado.')
            input('\nPressione uma tecla para continuar...')
        case '5':
            # READ (LER / CONSULTAR / BUSCAR)
            print('== BUSCAR PRODUTO ==')
            nome = input('Qual produto deseja buscar? ').strip().upper()
            if nome in lista_produtos:
                print('Produto encontrado!')
            else:
                print('Este produto não está no estoque.')
            input('\nPressione uma tecla para continuar...')
        case '0':
            print('Saindo do programa...')
            break
        case _:
            input('Opção Inválida\nAperte qualquer botão para voltar ao menu...')


