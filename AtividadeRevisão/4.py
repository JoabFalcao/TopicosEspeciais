valor = list(map(int, input("Adicione 15 valores.").split()))
maior = valor[0]; posicao = int()
for i in range(1, 15):
	if valor[i] > maior:
		maior = valor[i]
		posicao = i		
print ("Maior valor {} está em {}." .format(maior, posicao + 1))
