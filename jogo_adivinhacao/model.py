CATEGORIAS = {
    "Frutas": ["banana", "morango", "abacaxi", "melancia"],
    "Cores": ["azul", "verde", "amarelo", "vermelho"],
    "Animais": ["cachorro", "elefante", "girafa", "tartaruga"],
    "Países": ["brasil", "portugal", "argentina", "japao"]
}

def get_categorias():
    return list(CATEGORIAS.keys())

def get_palavras_por_categoria(categoria):
    return CATEGORIAS.get(categoria, []).copy()