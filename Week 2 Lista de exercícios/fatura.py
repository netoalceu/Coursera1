cliente = input("Digite o nome do cliente: ")
dia_de_vencimento = input("Digite o dia de vencimento: ")
mês_de_vencimento = input("Digite o mês de vencimento: ")
valor_da_fatura = float(input("Digite o valor da fatura: "))

print("Olá, ",cliente)
print("A sua fatura com vencimento em ",dia_de_vencimento, " de ", mês_de_vencimento," no valor de R$ %.2f está fechada."% valor_da_fatura)
