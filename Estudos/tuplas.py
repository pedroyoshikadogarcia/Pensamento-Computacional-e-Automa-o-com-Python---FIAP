# A tupla é uma lista porém ela não e alteravel (nao da para mudar os itens dela

tupla =(1,2,3,4,5, 'pedro')

print(tupla[5])

# Se quiser adicionar ou remover algo da tupla precisamos atribuir novamente os valores dela:

tupla = (1,2,3,4,5,'feijao') # O item novo é o feijao, se executarmos:
print(tupla)

# Utilizando a Tupla

cliente = ('Joao', '12345678900', '111111111') #Informações que nao podem ser mudadas (rg e cpf)
#Caso queira criar uma listea de clientes utiliza-se listas
clientes = []
clientes.append(cliente) #Pega a lista clientes e adiciona a tupla cliente
print(clientes)

# Adicionando um novo cliente
cliente = ('Pedro', '1111111111111',' 11111111111') #Agora adicionamos o cliente dentro da lista clientes
clientes.append(cliente)
print("Agora com o novo cliente: ", clientes)

# Para acessar os clientes na lista:
print("Chamando o cliente 1: ",clientes[0])

# Tuplas com Dicionario

capitais = {
    ('Brasil', 'São Paulo'): 'São Paulo', # Junta o dicionario com tupla o 'Brasil','São Paulo' é uma tupla que seria uma chave e o #'Sao paulo dps dos : é o valor
    ('Brasil', 'Rio de Janeiro'): 'Rio de Janeiro',
    ('Brasil', 'Minas Gerais'): 'Belo Horizonte'
} # Foi criado um dicionario de capitais onde cada chave representa o pais e o estado
print(capitais.keys()) # O metodo keys perite pegar todas as chaves do dicionario
print(capitais.values()) # O metodo values permite pegar todos os valores do dicionario

# Métodos de tuplas
tupla = (1,2,3,4,5,6,1)
print(tupla.index(3)) # O index me da a posicao de alguma coisa q eu esteja procrando na tupla <- estou procurando a posicao do item 3
print(tupla.count(1)) # Conta quantas vezes o item apareceu na minha tupla

#Desafio: Criando um gerenciador de cadastro de materiais

lista_materiais = []

def cadastrar_materiais(nome, codigo, unidade, quantidade): #Defini as variaveis dentro da "funcao"
    tupla = (nome, codigo, unidade, quantidade) # Cria a tupla com as mesmas variaveis que coloquei no ()
    lista_materiais.append(tupla) # Adiciona a Tupla na lista de materiais
    return lista_materiais # O return sempre fecha a função.

def consultar_materiais(codigo): # Funcao de consulta do codigo
    for material in lista_materiais:
        if material[1] == codigo:
            return material
        else:
            pass
cadastrar_materiais('Borracha', 1, 'un', 500) #Cadastrando os itens na lista chamando a funcao e dando a informacao na tupla da funcao
cadastrar_materiais('Tesoura', 2, 'un', 500)
print(lista_materiais)
print(consultar_materiais(1)) # Puxa o material pelo codigo