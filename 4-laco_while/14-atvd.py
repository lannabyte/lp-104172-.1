import os
os.system('cls')

soma_salarios = 0
quantidade = 0
maior_idade = 0
menor_idade = 0
mulheres_5000 = 0

while True:

    print("===== MENU =====")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:

        idade = int(input("Digite a idade: "))
        sexo = input("Digite o sexo (M/F): ").upper()
        salario = float(input("Digite o salário: R$ "))

        soma_salarios = soma_salarios + salario
        quantidade = quantidade + 1

        if quantidade == 1:
            maior_idade = idade
            menor_idade = idade
        else:
            if idade > maior_idade:
                maior_idade = idade

            if idade < menor_idade:
                menor_idade = idade

        if sexo == "F" and salario >= 5000:
            mulheres_5000 = mulheres_5000 + 1

        os.system("cls" if os.name == "nt" else "clear")

    elif opcao == 2:

        if quantidade > 0:
            media = soma_salarios / quantidade

            print("===== RESULTADOS =====")
            print("Média salarial: R$", media)
            print("Maior idade:", maior_idade)
            print("Menor idade:", menor_idade)
            print("Mulheres com salário a partir de R$ 5.000:", mulheres_5000)
        else:
            print("Nenhuma pessoa foi cadastrada.")

    elif opcao == 3:
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")