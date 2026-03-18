#Valor gasto

s = float(input("Digite o seu saldo: "))
livro = int(25)
caneta = int(5)

qtdl = livro * 3
qtdc = caneta * 2
gastoT = qtdl + qtdc
gasto = s - gastoT


print(f"O seu gasto foi de {gasto} reais")