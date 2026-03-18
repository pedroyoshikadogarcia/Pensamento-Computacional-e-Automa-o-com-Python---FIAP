#Peça 1

nome1 = input("Nome da peça 1: ")
qtd1 = int(input(f"Quantidade de {nome1}: "))
valor1 = float(input(f"Valor unitário de {nome1}: "))

#Peça 2

nome2 = input("Nome da peça 1: ")
qtd2 = int(input(f"Quantidade de {nome2}: "))
valor2 = float(input(f"Valor unitário de {nome2}: "))

total = (qtd1 * valor1) + (qtd2 * valor2)

print(f"Valor a pagar: {total}")