numero = int(input("Digite numero fatorial: "))
fatorial = 1
for termo in range(1, numero + 1):
    fatorial *= termo
print(f"fatorial de {numero}! é {fatorial}")