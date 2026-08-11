eng2sp = dict()
print(eng2sp)

eng2sp["one"] = 'uno'
print(eng2sp)

eng2sp = {
    'one' : 'uno',
    'two' : 'dos',
    'three' : 'tres'
}
print(eng2sp)
print(eng2sp['two'])

#Operador IN

print('dos' in eng2sp)

#Verificar os valors do dict

valores = eng2sp.values()
print ('uno' in valores)

#Contador de Letras

def count_letters(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

dict_contagem = count_letters("ovo")
print (dict_contagem)

# TUPLA é uma lista que os elementos não podem ser alterados

