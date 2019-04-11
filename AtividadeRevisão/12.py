def valorPagamento(prestacao, atraso):
	valor = int()
	if atraso == 0:
		valor = prestacao
	elif atraso > 0:
		valor = prestacao + (prestacao * 0.03) + ((prestacao * 0.001) * atraso)
	return (valor)	
prestacao = float(input("Valor da prestação: "))
while prestacao > 0:
	atraso = int(input("Período de dias em atraso: "))
	print ("Valor total: R$ {:.2f}" .format (valorPagamento(prestacao, atraso)))
	prestacao = float(input("Valor da prestação.R$ "))	
