import random
import model


def obter_lista_categorias():
    return model.get_categorias()


def obter_quantidade_palavras(categoria):
    palavras = model.get_palavras_por_categoria(categoria)
    return len(palavras)


def selecionar_palavra(categoria, posicao):
    palavras = model.get_palavras_por_categoria(categoria)
    random.shuffle(palavras)

    if 1 <= posicao <= len(palavras):
        return palavras[posicao - 1]
    return None


def criar_estado_jogo(palavra_secreta):
    return {
        "palavra_secreta": palavra_secreta.lower(),
        "letras_descobertas": [],
        "letras_tentadas": [],
        "tentativas_restantes": 6,
        "venceu": False,
        "perdeu": False
    }


def processar_tentativa(estado, letra):
    letra = letra.lower().strip()

    if not letra or len(letra) != 1 or not letra.isalpha():
        return False, "Por favor, digite apenas uma letra válida."

    if letra in estado["letras_tentadas"]:
        return False, "Você já tentou essa letra!"

    estado["letras_tentadas"].append(letra)

    if letra in estado["palavra_secreta"]:
        estado["letras_descobertas"].append(letra)
        if toda_palavra_descoberta(estado):
            estado["venceu"] = True
        return True, "Você acertou uma letra!"
    else:
        estado["tentativas_restantes"] -= 1
        if estado["tentativas_restantes"] <= 0:
            estado["perdeu"] = True
        return False, "Você errou!"


def formatar_palavra_oculta(estado):
    palavra = estado["palavra_secreta"]
    revelada = ""
    for char in palavra:
        if char in estado["letras_descobertas"]:
            revelada += char
        else:
            revelada += "_"
    return revelada


def toda_palavra_descoberta(estado):
    for char in estado["palavra_secreta"]:
        if char not in estado["letras_descobertas"]:
            return False
    return True