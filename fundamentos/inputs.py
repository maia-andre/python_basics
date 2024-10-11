# nome = input("Escreva seu nome: ")
# email = input("Escreva seu email: ")
# print(nome,email)

# faturamento = float(input("Escreva seu faturamento: "))
# imposto = faturamento * 0.1
# print(faturamento,imposto)

#listas

# vendas = [100, 50, 14, 20, 30, 700]

#soma dos elementos
# total_vendas = sum(vendas)
# print(total_vendas)

# tamanho da lista
# quantidade_vendas = len(vendas)
# print(quantidade_vendas)

# max e min
# print(max(vendas))
# print(min(vendas))

# pegar posição
# print(vendas[5])

listas_produtos = ["iphone", "airpod", "apple watch", "macbook"]
print(listas_produtos)
# produto_procurado = input("Pesquise pelo nome do produto: ")
# produto_procurado = produto_procurado.lower()

# print(produto_procurado in listas_produtos)

# adicionar um item na lista

listas_produtos.append("ipod")
print(listas_produtos)

# remover um item da lista
listas_produtos.remove("airpod")
print(listas_produtos)

listas_produtos.pop(0)
print(listas_produtos)

# editar um item
precos = [1000, 1500, 3500]
precos[0] = precos[0] * 1.5
print(precos)

# contar quantas vezes o item aparece na lista
produtos = ["iphone", "airpod", "apple watch", "macbook", "iphone", "airpod", "iphone", "macbook"]
print(produtos.count("iphone"))

# ordenar uma lista - se colocar reverse=True no arg no sort, ele dá a lista ao contrário

produtos.sort()
print(produtos)