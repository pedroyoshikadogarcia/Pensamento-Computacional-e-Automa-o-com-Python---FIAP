nomes = ["Ale", "Joao", "max", "Bob"]

for i in range (len(nomes)):
    for j in range(i + 1, len(nomes)):
        print(f"{nomes[i]} e {nomes[j]}")
