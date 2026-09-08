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
    pontos[jogador] = valor

campeao = " "
for jogador in pontos:
    if pontos[jogador] > pontos[campeao]:
        campeao = jogador


print(pontos)
print(campeao)