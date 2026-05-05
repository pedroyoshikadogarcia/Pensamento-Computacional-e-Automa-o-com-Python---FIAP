lista_frutas = ["Abacaxi", "Banana", "Mamão"]

print(lista_frutas[2])

#adicionando mais um elemento na lista - .append adiciona o item no final da lista

lista_frutas.append("Uva")
print(lista_frutas[3])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])
print()

for fruta in lista_frutas:
    print(fruta)