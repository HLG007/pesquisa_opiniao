excelente = 0
bom = 0
ruim = 0

pesquisas = 50

for i in range(pesquisas):
    nome = input("Qual seu nome? ")
    idade = int(input("Qual sua idade? "))
    resposta = input("Entre excelente, bom e ruim. Como você avalia o atendimento? ")
    if resposta == "excelente":
        excelente += 1
    elif resposta == "bom":
        bom += 1
    else:
        ruim += 1

    print("obrigado pela pesquisa!")

print(f"excelentes: {excelente}, bom: {bom}, ruim: {ruim}")