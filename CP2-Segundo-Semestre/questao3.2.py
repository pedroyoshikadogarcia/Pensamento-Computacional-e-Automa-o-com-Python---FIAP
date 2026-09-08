partidas = (
    ("Ana" , 10),
    ("Bruno", 7),
    ("Carlos", 8),
    ("Ana", 5),
    ("Bruno", 10),
    ("Carlos", 4),
    ("Ana", -2)
)

pontos = {}

for jogador, valor in partidas:
    if jogador not in pontos:
        pontos[jogador] = 0

        pontos [jogador] += valor

campeao = " "
for jogador in pontos:
    campeao = jogador

print(pontos)
print(campeao)