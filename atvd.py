import os

cardapio = {
   "1": ["Picanha", 25.00],
   "2": ["Lasanha", 20.00],
   "3": ["Strogonoff", 18.00],
   "4": ["Bife Acebolado", 15.00],
   "5": ["Pao com ovo", 5.00]
}

pedidos = []
continuar = "S"

while continuar == "S":

   print("\n===== CARDAPIO =====")

   for codigo in cardapio:
       print(codigo, "-", cardapio[codigo][0],
             "- R$", cardapio[codigo][1])

   codigo = input("\nDigite o codigo: ")

   if codigo in cardapio:

       quantidade = input("Quantidade: ")

       if quantidade.isdigit() and int(quantidade) > 0:
           pedidos.append([codigo, int(quantidade)])
           print("Pedido adicionado!")

       else:
           print("Quantidade invalida!")

   else:
       print("Codigo invalido!")

   continuar = input("Deseja outro prato? (S/N): ").upper()

   while continuar != "S" and continuar != "N":
       continuar = input("Digite S ou N: ").upper()


# Remover pedidos
remover = "S"

while remover == "S" and pedidos != []:

   contador = 1

   for item in pedidos:
       print(contador, "-", cardapio[item[0]][0])
       contador += 1

   remover = input("Deseja remover algum item? (S/N): ").upper()

   if remover == "S":

       escolha = input("Numero do item: ")

       if escolha.isdigit():

           escolha = int(escolha)
           nova_lista = []
           contador = 1

           for item in pedidos:

               if contador != escolha:
                   nova_lista.append(item)

               contador += 1

           if escolha >= 1 and escolha < contador:
               pedidos = nova_lista
               print("Item removido!")
           else:
               print("Item inexistente!")

       else:
           print("Digite um numero valido!")


# Fechamento da conta
total = 0

print("\n===== RESUMO DO PEDIDO =====")

for item in pedidos:

   codigo = item[0]
   quantidade = item[1]

   nome = cardapio[codigo][0]
   preco = cardapio[codigo][1]

   subtotal = preco * quantidade
   total += subtotal

   print(nome, "-", quantidade, "unidade(s)",
         "- R$", subtotal)


print("\nSubtotal: R$", total)

taxa = input("Aceita 10% de taxa de serviço? (S/N): ").upper()

while taxa != "S" and taxa != "N":
   taxa = input("Digite S ou N: ").upper()

if taxa == "S":
   valor_taxa = total * 0.10
else:
   valor_taxa = 0

total_final = total + valor_taxa

print("\nTaxa: R$", valor_taxa)
print("TOTAL: R$", total_final)
print("Obrigado pela preferencia!")
print("Volte sempre.")