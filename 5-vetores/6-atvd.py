import os

elenco = []

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=== GERENCIAMENTO DE ELENCO ===")
    print("1. Cadastrar jogador")
    print("2. Listar jogadores")
    print("3. Atualizar jogador")
    print("0. Sair")
    
    opcao = input("\nEscolha uma opção: ").strip()

    # 1. CREAD (CADASTRAR)
    if opcao == '1':
        print("\n-- CADASTRAR JOGADOR --")
        nome = input("Nome: ").strip()
        posicao = input("Posição: ").strip()
        camisa = input("Camisa: ").strip()

        if nome == "" or posicao == "" or camisa == "":
            print("Erro: Nenhum campo pode ficar em branco!")
        elif not camisa.isdigit():
            print("Erro: A camisa deve ser um número!")
        else:
            # Salva tudo junto em uma única linha de texto
            jogador = f"{nome} | {posicao} | #{camisa}"
            elenco.append(jogador)
            print("Jogador cadastrado com sucesso!")

        input("\nPressione Enter para continuar...")

    # 2. READ (LISTAR)
    elif opcao == '2':
        print("\n-- LISTA DE JOGADORES --")
        if len(elenco) == 0:
            print("O elenco está vazio.")
        else:
            for i, jogador in enumerate(elenco):
                print(f"{i + 1}. {jogador}")

        input("\nPressione Enter para continuar...")

    # 3. UPDATE (ATUALIZAR)
    elif opcao == '3':
        print("\n-- ATUALIZAR JOGADOR --")
        if len(elenco) == 0:
            print("O elenco está vazio.")
        else:
            # Exibe a lista para o usuário saber qual número escolher
            for i, jogador in enumerate(elenco):
                print(f"{i + 1}. {jogador}")

            numero_str = input("\nDigite o número do jogador que deseja alterar: ").strip()

            if numero_str.isdigit():
                numero = int(numero_str)
                
                # Verifica se o número existe na lista
                if 1 <= numero <= len(elenco):
                    posicao_index = numero - 1
                    
                    print("\nDigite os novos dados:")
                    novo_nome = input("Novo Nome: ").strip()
                    nova_posicao = input("Nova Posição: ").strip()
                    nova_camisa = input("Nova Camisa: ").strip()

                    if novo_nome == "" or nova_posicao == "" or nova_camisa == "":
                        print("Erro: Nenhum campo pode ficar em branco!")
                    elif not nova_camisa.isdigit():
                        print("Erro: A camisa deve ser um número!")
                    else:
                        # Substitui o item antigo pelo novo
                        elenco[posicao_index] = f"{novo_nome} | {nova_posicao} | #{nova_camisa}"
                        print("Jogador atualizado com sucesso!")
                else:
                    print("Erro: Número de jogador inválido!")
            else:
                print("Erro: Digite apenas números!")

        input("\nPressione Enter para continuar...")

    # 0. SAIR
    elif opcao == '0':
        print("\nSaindo do programa...")
        break

    else:
        input("\nOpção inválida! Pressione Enter para tentar novamente...")