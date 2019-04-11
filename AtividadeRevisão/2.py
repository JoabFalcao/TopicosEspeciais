valor = list(map(int, input("Adicione 6(seis) valores.").split()))
valorPositivo = int()

for i in valor:
	
	if i > 0:		
		valorPositivo += 1
		
print ("Os valores positivos {}." .format(valorPositivo))	
