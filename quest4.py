nota = float(input("Digite a nota: "))
faltas = float(input("Digite a faltas: "))

if nota >= 7 and faltas <= 5:
            print("Aprovado")
elif nota >= 5 and faltas <= 10:
            print("Reculperação")
else:
            print("Reprovado")
