# Dicionario é uma lista de valores com rótulo

email_gerentes={
    "Iguatemi" : "iguatemi@email.com", # Chave : valor
    "Plaza" : "plaza@email.com",
    "Barra" : "barra@emai.com"
}

# Principais métodos:
email = email_gerentes["Iguatemi"] # Chama achave iguatemi e ele me tras o valor do iguatemi
print(email)

email_gerentes["Aricanduva"] = "aricanduva@email.com" # Para adicionar o item no dicionario (se ja existir o item ele substitui
print(email_gerentes)

# Como descobrir todos as chaves do dicionario (2 maneiras)

for shopping in email_gerentes:
    print(shopping)

print(email_gerentes.keys())

# Como printar todos os valores do dicionario (2 formas)

for shopping in email_gerentes:
    email = email_gerentes[shopping]
    print(email)

print(email_gerentes.values())

# Como retirar uma key

email_gerentes.pop("Barra")
print(email_gerentes)

# Verificar se o item existe no dicionario

if "Iguatemi" in email_gerentes:
    print("Existe")
else:
    print("Não existe")

if "iguatemi@email.com" in email_gerentes.values():
    print("Existe")
else:
    print("Não existe")