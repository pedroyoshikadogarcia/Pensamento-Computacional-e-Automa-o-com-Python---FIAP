escolha_usuario = 1

# 0 -> Sair do programa
# 1 -> Entrar no Programa
# >>> ERRO

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entrar no programa")
    case _:
        print("Erro")