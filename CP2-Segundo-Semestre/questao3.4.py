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
        pontos[jogador] = valor
    else:
        pontos[jogador] = pontos[jogador] + valor

campeao = ""
maior_pontuacao = 0

for jogador in pontos:

    if pontos[jogador] >= maior_pontuacao:
        maior_pontuacao = pontos[jogador]
        campeao = jogador

print(pontos)
print(campeao)