lista_precos = [1500, 1000, 800, 3000]

#variaveis criadas dentro da função só existem dentro dela

def calcula_imposto_total(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    impost_iss = 0.15 * preco
    imposto_csll = 0.05 * preco
    imposto_total = imposto_ir + impost_iss + imposto_csll
    return imposto_total

for preco in lista_precos:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco}: R$ {imposto_total}")

nova_lista = [5000, 2000, 6000, 7000, 1000]

for preco in nova_lista:
    imposto_total = calcula_imposto_total(preco)
    print(f"Imposto total sobre o produto de R$ {preco}: R$ {imposto_total}")
