#Logica E (and)

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Logado com sucesso")

#Logica OU (or)

logica_ou = False or True
print(logica_ou)

#Operador NOT

negacao = not False
print(negacao)

if not verifica_login:
    print("Seu login ou senha estão errados")