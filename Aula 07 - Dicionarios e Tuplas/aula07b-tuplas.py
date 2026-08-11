# TUPLA é uma lista que os elementos não podem ser alterados

t = ('a', 'b', 'c', 'd')
print(type(t))

t = tuple("Fiap")
print(t)
print(t[1:5])

#Atribuição de TUPLAS

a = 1
b = 2
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

email = "fulano@gmail.com"
usuario , dominio = email.split("@")

print (usuario)
print(dominio)