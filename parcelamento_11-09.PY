import os
os.system('cls ||  clear')

produto= float(input("Digite o valor do produto: "))
print("\nForma de pagamento: ")
print("1 - Pagamento a vista")
print("2 - Pagamento a prazo")
forma = int(input("Escolha a forma (1 ou 2): "))

#OPÇÃO 1- A VISTA COM 10% DE DESCONTO

if forma == 1:
    desconto = produto * 0.10
    total = produto

    print("\n--- PAGAMENTO Á VISTA ---")
    print(f"Valor do produto: R$ {produto:.2f}")
    print(f"Forma de pagamento: á vista")
    print(f"Valor do desconto: R$ {desconto: .2f}")
    print(f"Total a pagar: R$ {total: .2f}")

#OPÇÃO 2- A PRAZO PARCELADO EM ATE 6X

elif forma == 2:
    parcelas = int(input("Digite a quantidade de parcelas (atr 6X): "))

    if parcelas < 1 or parcelas > 6:
        print("Erro! parcelas apenas em ate 6 vezes. ")
        exit() # FIM DO PROGRAMA.

    else:
        valor_parcela = produto / parcelas

        print("\n--- PAGAMENTO A PRAZO ---")
        print(f"Valor do produto: R$ {produto: .2f}")
        print(f"Forma de pagamento: a prazo")
        print(f"Quantidade de parcelas: {parcelas}")
        print(f"Valor por parcelas: R$ {valor_parcela:.2f}")
        print(f"Total a prazo: R$ {produto:.2f}")

else:
    print("Opção de pagamento inválida")
