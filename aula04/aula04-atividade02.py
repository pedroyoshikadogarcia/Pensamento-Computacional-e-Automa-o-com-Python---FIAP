def verificar_nota(nota):
    while nota < 0 or nota > 10:
        print("Nota digitada invalida. Digite uma nota de 0 a 10.")
        nota = float(input(f"Digite a nota novamente: "))
    return nota

notaA = float(input("Digite a 1º nota: "))
notaA = verificar_nota(notaA)
notaB = float(input("Digite a 2º nota: "))
notaB = verificar_nota(notaB)

media = (notaA + notaB) / 2
print(media)