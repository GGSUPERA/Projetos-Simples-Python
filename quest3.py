idade = float(input("Digite sua idade: "))
ingresso = str(input("Tem ingresso sim-y ou não-n: "))

if idade >= 18 and ingresso == "y":
    print("Pode entrar")
elif idade >= 18 and ingresso == "n":
    print("Sem ingresso não entra")
else:
    print("Não pode entrar")