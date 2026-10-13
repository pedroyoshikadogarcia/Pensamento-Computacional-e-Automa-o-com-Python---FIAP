class Inversor:
    def __init__(self, modelo, potencia):
        self.modelo = modelo
        self.potencia = potencia
        self.leituras = []

    def registrar(self, valor):
        self.leituras.append(valor)
        return len(self.leituras)

inv1 = Inversor("GW5000", 5000)
inv2 = inv1
inv3 = Inversor("GW5000", 5000)

inv2.registrar(1200)
inv1.registrar(800)
total = inv3.registrar(300)

print(len(inv1.leituras), len(inv3.leituras), total)