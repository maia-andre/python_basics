vendas = 3000
meta1 = 1200
meta2 = 2000
meta_empresa = 10000
venda_empresa = 12000
# operadores de comparação: > < >= <= == !=

# primeira forma de aplicar if else
#if vendas >= meta2:
#    print("Bateu a maior meta! Receba seu bônus!")
#    bonus = 0.13 * vendas
#    print("Seu bônus é de: ", bonus)
# else:
#    if vendas >= meta1:
#        print("Bateu a primeira meta! Receba seu bônus!")
#        bonus = 0.1 * vendas
#        print("Seu bônus é de: ", bonus)
#    else:
#        bonus = 0
#        print("Vendedor não bateu a meta e não ganha bônus = ", bonus)    

# segunda forma de aplicar if elif else
# entre um if e else, vc pode ter quantos elif quiser
# and serve para acrescentar mais de uma condições / or serve para que atendida uma das condições, o retorno seja true

if vendas >= 2000 and venda_empresa >= meta_empresa:
    bonus = 0.13 * vendas
    print("Seu bonus é de: ", bonus)
elif vendas >= 1300 and venda_empresa >= meta_empresa:
    bonus = 0.10 * vendas
    print("Seu bonus é de: ", bonus)
else:
    bonus = 0
    print("Seu bônus é de: ", bonus)    

produtos = ["airpod", "macbook", "iphone", "ipod"]
produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in produtos:
    print("Disponível no estoque")
else:
    print("Indisponível no estoque")