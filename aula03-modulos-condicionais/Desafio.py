idade = int((input('Digite sua idade: ')))

if idade >= 16 and idade <18:
    print('O seu voto é opcional')
elif idade >= 18 and idade <70:
    print('O seu voto é obrigatório')
else:
    print('O seu voto é opcional')