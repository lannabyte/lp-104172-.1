import os

lista_pacientes = []

while True:
    os.system('cls')
    # Menu do programa.
    print('''
    === CADASTRO DE PACIENTES - HOSPITAL ===
    1 - Cadastrar paciente
    2 - Listar pacientes
    3 - Atualizar paciente
    4 - Remover paciente
    5 - Buscar paciente
    0 - Sair
    ''')
    opcao = input('Escolha uma opção: ')

    match opcao:
        case '1':
            # CREATE (CRIAR)
            print('\n== CADASTRAR PACIENTE ==')
            nome = input('Nome: ').strip().upper()
            sobrenome = input('Sobrenome: ').strip().upper()

            if nome == '' or sobrenome == '':
                print('Erro: Nome e sobrenome não podem ficar em branco.')
            else:
                paciente_completo = f"{nome} {sobrenome}"
                if paciente_completo in lista_pacientes:
                    print(f'{paciente_completo} já está cadastrado.')
                else:
                    lista_pacientes.append(paciente_completo)
                    print('Paciente cadastrado com sucesso!')

            input('\nPressione uma tecla para continuar...')

        case '2':
            # READ (LISTAR)
            print('\n== LISTA DE PACIENTES ==')
            if len(lista_pacientes) == 0:
                print('Não há pacientes cadastrados.')
            else:
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i+1}º Paciente: {paciente}")
                print(f'\nTotal de pacientes: {len(lista_pacientes)}')

            input('\nPressione uma tecla para continuar...')

        case '3':
            # UPDATE (ATUALIZAR POR NÚMERO)
            print('\n== ATUALIZAR PACIENTE ==')
            if len(lista_pacientes) == 0:
                print('Não há pacientes cadastrados para atualizar.')
            else:
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i+1}º Paciente: {paciente}")

                numero_str = input('\nDigite o NÚMERO do paciente que deseja atualizar: ').strip()

                if numero_str.isdigit():
                    numero = int(numero_str)
                    if 1 <= numero <= len(lista_pacientes):
                        posicao = numero - 1
                        novo_nome = input('Novo nome: ').strip().upper()
                        novo_sobrenome = input('Novo sobrenome: ').strip().upper()

                        if novo_nome == '' or novo_sobrenome == '':
                            print('Erro: Nome e sobrenome não podem ficar em branco.')
                        else:
                            lista_pacientes[posicao] = f"{novo_nome} {novo_sobrenome}"
                            print('Paciente atualizado com sucesso!')
                    else:
                        print('Número de paciente inexistente.')
                else:
                    print('Erro: Digite apenas números.')

            input('\nPressione uma tecla para continuar...')

        case '4':
            # REMOVE (EXCLUIR POR NÚMERO)
            print('\n== REMOVER PACIENTE ==')
            if len(lista_pacientes) == 0:
                print('Não há pacientes cadastrados para remover.')
            else:
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i+1}º Paciente: {paciente}")

                numero_str = input('\nDigite o NÚMERO do paciente que deseja remover: ').strip()

                if numero_str.isdigit():
                    numero = int(numero_str)
                    if 1 <= numero <= len(lista_pacientes):
                        posicao = numero - 1
                        removido = lista_pacientes.pop(posicao)
                        print(f'Paciente {removido} removido com sucesso!')
                    else:
                        print('Número de paciente inexistente.')
                else:
                    print('Erro: Digite apenas números.')

            input('\nPressione uma tecla para continuar...')

        case '5':
            # READ (BUSCAR)
            print('\n== BUSCAR PACIENTE ==')
            if len(lista_pacientes) == 0:
                print('Não há pacientes cadastrados para busca.')
            else:
                termo = input('Digite o nome ou sobrenome para buscar: ').strip().upper()

                if termo == '':
                    print('O termo de busca não pode ser vazio.')
                else:
                    encontrados = 0
                    for i, paciente in enumerate(lista_pacientes):
                        if termo in paciente:
                            print(f"{i+1}º Paciente: {paciente}")
                            encontrados += 1

                    if encontrados == 0:
                        print('Nenhum paciente encontrado com esse nome/sobrenome.')

            input('\nPressione uma tecla para continuar...')

        case '0':
            print('\nSaindo do programa...')
            break

        case _:
            input('\nOpção Inválida!\nAperte qualquer botão para voltar ao menu...')