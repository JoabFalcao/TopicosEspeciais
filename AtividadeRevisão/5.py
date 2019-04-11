valor = list(map(int, input("Adicione 6(seis) valores.").split()))
valorPositivo = int()
mediaTotal = int()

for i in valor:
	
	if i > 0:		
		valorPositivo += 1
		mediaTotal += i
		
print ("A quantidade de valores positivos são {}. Com a média: {:.1f}" .format( valorPositivo, mediaTotal / valorPositivo))	
