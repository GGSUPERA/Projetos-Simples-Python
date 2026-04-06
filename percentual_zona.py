largura_garagem = float(input('Largura da garagem em metros: '))
profundidade_garagem = float(input('Profundidade em metros: '))

area_garagem = largura_garagem * profundidade_garagem#Calculo da area da garagem

largura_Terreno = float(input('Largura da terreno em metros: '))
profundidade_Terreno = float(input('Profundidade em metros: '))

area_terreno = largura_Terreno * profundidade_Terreno#Calculo da area da terreno

percentual = (area_garagem / area_terreno) * 100#Calculo do percentual

Zona = input('Entre com a Zona Norte-N, Sul-S, Leste-L e Oeste-O: ')

print(f"Zona Escolhida: {Zona}")
print(f"Percentual da Zona: {percentual}%")

if Zona == "N" and percentual <= 25:
    print('A zona atende aos requerimentos do plano diretor')
elif Zona == "L" or Zona == "O" and percentual <= 30:
    print('A zona atende aos requerimentos do plano diretor')
elif Zona == "S" and percentual <= 40:
    print('A zona atende aos requerimentos do plano diretor')
else:
    print('A zona NÃO atende aos requerimentos do plano diretor')

