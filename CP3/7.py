geracao = [
    [3, 5, 0, 4],
    [0, 0, 0, 6],
    [7, 1, 0, 0]
]

resultado = []

for i in range(len(geracao)):
    zeros = 0
    for j in range(len(geracao[i])):
        if geracao[i][j] == 0:
            zeros += 1
            if zeros >=2:
                resultado.append(i)
                break
        else:
            zeros = 0

print(resultado)