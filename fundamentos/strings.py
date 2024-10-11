faturamento = 1000
custo = 700
lucro = faturamento - custo
margem_lucro = lucro / faturamento

print("Faturamento aguardado: {}, Custo: {}, Lucro: {}".format(faturamento, custo, lucro))
print(f"Faturamento aguardado: {faturamento}, Custo: {custo}, Lucro: {lucro}")

# print("O faturamento foi de ", faturamento)
# print("O custo foi de ", custo)
# print("O lucro foi de", lucro)
# print("A margem de lucro foi de", margem_lucro)

email = "andre@sjc.sp.gov.br"
email = email.upper()
print(email)
email = email.lower()
print(email)

print(email.find("@")) # -1 quando não encontrado

print(len(email)) # len conta o tamanho do texto

print(email[:5]) # colchete serve para mostrar algo específico da string 
# caso tente um número maior do que o tamanho do texto, ele dará erro out of range
# se usar números negativos, ele começa de trás pra frente
# utilize : para pegar do ínicio até o número do índice indicado. Ex. 0:5

novo_email = email.replace("sjc.sp.gov.br", "gmail.com") 
#caso ele não encontre o texto para substituir, ele não dá erro, ele só não faz nada
print(novo_email)

nome = "andré maia"
print(nome.title()) #title coloca a inicial de todas as palavras em maiúscula
print(nome.capitalize()) #capitalize coloca somente a inicial da primeira palavra em maiúscula

posicao_arroba = email.find("@")
servidor = email[posicao_arroba:]
print(servidor)

espaco = nome.find(" ")
primeiro_nome = nome[:espaco]
print(primeiro_nome.capitalize())

ultimo_nome = nome[espaco+1:]
print(ultimo_nome.capitalize())

margem_lucro = round(margem_lucro,2)
print(f"Faturamento aguardado: R$ {faturamento:.2f}, Custo: R$ {custo:.2f}, Lucro: R$ {lucro:.2f}, Margem: {margem_lucro:.0%}")