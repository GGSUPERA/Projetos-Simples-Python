tabua = float(input("Quantas taboas: "))
tamanho_largura = float(input("Largura da tabua: "))
tamanho_comprimento = float(input("Comprimento da tabua: "))

if tabua >= 20 and tamanho_largura <= 10 and tamanho_comprimento <= 10:
    print("Pacote completo")
    if tabua <= 10 and tamanho_largura <= 20 and tamanho_comprimento <= 20:
        print("Pacote grande completo")
elif tabua < 20 and tamanho_largura >= 10 and tamanho_comprimento >= 10:
    print(f"Falta {20 - tabua} tabuas e {20 - tamanho_largura}largura e {20 - tamanho_comprimento} comprimento tabuas")
elif tabua < 10 and tamanho_largura >= 20 and tamanho_comprimento >= 20:
    print(f"Falta {20 - tabua} tabuas ")
else:
    print(f"Retire {tabua - 20} tabuas")