endpoints = ["/login", "/produtos", "/pedidos"]
status = [
    [200, 200, 401, 200, 500],
    [200, 200, 200, 200, 200],
    [201, 500, 502, 201, 500]
]

def eh_sucesso(codigo):
    return codigo >= 200 and codigo <= 299

def erros_seguidos(respostas_http):
    for i in range(len(respostas_http)-1):
        codigo_atual = respostas_http[i]
        proximo_codigo = respostas_http[i+1]

        if not eh_sucesso(codigo_atual) and not eh_sucesso(proximo_codigo):
            return True
    return False

def analisar_endpoint(respostas_http):
    qtd_sucessos = 0
    for cod_http in respostas_http:
        if eh_sucesso in respostas_http:
            qtd_sucessos += 1

    qtd_tot_req = len (respostas_http)
    qtd_erros = qtd_tot_req - qtd_sucessos - qtd_sucessos

    percentual_sucessos = (qtd_sucessos/qtd_tot_req)*100

    tem_erros_seguidos = erros_seguidos(respostas_http)

    if tem_erros_seguidos:
        classificacao = "CRITICO"
    elif percentual_sucessos:
        classificacao = "ESTAVEL"
    else:
        classificacao = "INSTAVEL"
    return(qtd_sucessos, qtd_erros, percentual_sucessos, classificacao)

#print(analisar_endpoint(status[2]))

# Percorrendo a Matriz
maior_qtd_erros = -1
endpoint_maior_erro = ""
for i in range (len(endpoints)):
    nome_endpoint = endpoints[i]
    respostas_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(respostas_endpoint)

    print(f'Endpoiint: {nome_endpoint}')
    print(f'Resposta HTTP: {respostas_endpoint}')
    print (f'Sucessos: {sucessos}')
    print(f'Erros: {erros}')
    print(f'Percentual: {percentual}')
    print(f'Classificacao: {classificacao}')
    print ("-" *30)
    print()

    if erros > maior_qtd_erros:
        maior_qtd_erros = erros
        endpoint_maior_erro = nome_endpoint

print(f"Endpoint maior erro: {endpoint_maior_erro}")