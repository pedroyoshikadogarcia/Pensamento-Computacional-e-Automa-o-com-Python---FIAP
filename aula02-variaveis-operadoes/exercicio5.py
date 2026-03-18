distanciaKm = 150
velocidadeKmh = 60

tempoKm = distanciaKm / velocidadeKmh

horas = int(tempoKm)
minutos = int((tempoKm - horas) * 60)

print(f"O carro levou {tempoKm} horas")
print(f"Então o tempo percorrido foi de {horas} horas e {minutos} minutos")