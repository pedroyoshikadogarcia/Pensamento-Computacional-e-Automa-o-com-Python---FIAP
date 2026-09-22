import control


def escolher_categoria():
    categorias = control.obter_lista_categorias()
    print("\nEscolha uma categoria:")
    for i, cat in enumerate(categorias, start=1):
        print(f"{i} - {cat}")

    while True:
        try:
            opcao = int(input("Digite a opção: "))
            if 1 <= opcao <= len(categorias):
                return categorias[opcao - 1]
            else:
                print("Opção inválida! Escolha um número da lista.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


def escolher_posicao(categoria):
    total = control.obter_quantidade_palavras(categoria)
    print(f"\nA categoria '{categoria}' possui {total} palavras.")

    while True:
        try:
            posicao = int(input(f"Escolha a posição da palavra (1 a {total}): "))
            if 1 <= posicao <= total:
                return posicao
            else:
                print(f"Posição inválida! Escolha um número entre 1 e {total}.")
        except ValueError:
            print("Entrada inválida! Digite um número.")


def jogar():
    categoria = escolher_categoria()
    posicao = escolher_posicao(categoria)

    palavra_secreta = control.selecionar_palavra(categoria, posicao)
    estado = control.criar_estado_jogo(palavra_secreta)

    print("\n" + "=" * 40)
    print("Você terá 6 tentativas para descobrir a palavra.")
    print("=" * 40)

    while not estado["venceu"] and not estado["perdeu"]:
        print(f"\nPalavra: {control.formatar_palavra_oculta(estado)}")
        print(f"Tentativas restantes: {estado['tentativas_restantes']}")

        letra = input("Digite uma letra: ")
        sucesso, mensagem = control.processar_tentativa(estado, letra)

        print(mensagem)

    if estado["venceu"]:
        print(f"\nParabéns! Você descobriu a palavra: {estado['palavra_secreta']}")
    elif estado["perdeu"]:
        print(f"\nSuas 6 tentativas terminaram.")
        print(f"A palavra era: {estado['palavra_secreta']}")


def main():
    while True:
        jogar()
        denovo = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if denovo != 's':
            print("Obrigado por jogar!")
            break


if __name__ == "__main__":
    main()