largura_garagem=float(input('Largura da garagem em metros:'))
profundidade_garagem=float(input('Profundidade em metros:'))
area_garagem=largura_garagem * profundidade_garagem#Calculo da area da garagem

largura_Terreno=float(input('Largura da terreno em metros:'))
profundidade_Terreno=float(input('Profundidade em metros:'))#
area_terreno= largura_Terreno * profundidade_Terreno#Calculo da area da terreno

percentual=(area_garagem / area_terreno) * 100#Calculo do percentual
print(f'Seu percentual é: {percentual}%')#Mostra o resultado