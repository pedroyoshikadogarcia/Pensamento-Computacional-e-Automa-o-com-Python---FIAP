#media ponderada

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

peso1 = 4
peso2 = 6

media = (n1 * peso1 + n2 * peso2) / (peso1 + peso2)

print(f"Media ponderada: {media}")