import os 
os.system('cls')

total_familias = 0
soma_salarios = 0
soma_filhos = 0
maior_salario = 0
menor_salario = 0

opcao = 0

while opcao != 2:
    print("\n1 - Adicionar família")
    print("2 - Sair e exibir resultados")

    opcao = int(input("Digite uma opção: "))

    if opcao == 1:
        salario = float(input("Digite o salário: R$ "))
        filhos = int(input("Digite o número de filhos: "))

        total_familias = total_familias + 1
        soma_salarios = soma_salarios + salario
        soma_filhos = soma_filhos + filhos

        if total_familias == 1:
            maior_salario = salario
            menor_salario = salario
        else:
            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario

    elif opcao == 2:
        if total_familias == 0:
            print("\nNenhuma família foi cadastrada.")
        else:
            media_salario = soma_salarios / total_familias
            media_filhos = soma_filhos / total_familias

            print("\n--- RESULTADOS ---")
            print("Total de famílias:", total_familias)
            print("Média dos salários: R$", media_salario)
            print("Média de filhos:", media_filhos)
            print("Maior salário: R$", maior_salario)
            print("Menor salário: R$", menor_salario)

    else:
        print("Opção inválida!")