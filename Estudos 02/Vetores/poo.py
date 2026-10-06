class CalculadoraMedia:
    def __init__(self, valores):
        self.valores = valores

    def processar(self):
        total = 0
        for i in range(len(self.valores)):
            total += self.valores[i]
        return total / len(self.valores)

numeros = [2, 4, 6, 8]
calc = CalculadoraMedia(numeros)
numeros.append(10)
print(calc.processar())