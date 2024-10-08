dict_produtos = {"airpod": 2000, "iphone": 6000, "ipad": 9000, "macbook": 12000}
# no valor do dicionario, vc pode colocar + valores utilizando colchetes

# buscar elemento
print(dict_produtos["airpod"])

# editar elemento
dict_produtos["airpod"] = dict_produtos["airpod"] * 1.3
print(dict_produtos)

# quantidade de itens
print(len(dict_produtos))

# retirar um item do dicionario
dict_produtos.pop("airpod")
print(dict_produtos)

# adicionar um item no dicionario
# dicionario não permite ter itens duplicados
# se vc tentar adicionar uma chave igual, ele irá substituir
dict_produtos["apple watch"] = 2500
print(dict_produtos)

# verificar se um item existe no dicionario
# primeiro por chave

#procurar = input("Digite o nome do produto: ")
#if procurar in dict_produtos:
#    print("O produto existe")
#else:
#    print("Produto não existe")

# procurar por valor
#if 9000 in dict_produtos.values():
#    print("Existe o valor")
#else:
#    print("Não existe")

# cadastrar novo produto a partir de input

# nome_produto = input("Digite o nome do produto: ")
# preco_produto = input("Digite o valor do produto: ")

#nome_produto = nome_produto.lower()
# preco_produto = float(preco_produto)

#dict_produtos[nome_produto] = preco_produto
#print(dict_produtos)

# colocar novo preco em todas chaves do dicionario

for produto in dict_produtos:
    novo_preco = dict_produtos[produto] * 1.1
    dict_produtos[produto] = novo_preco

print(dict_produtos)