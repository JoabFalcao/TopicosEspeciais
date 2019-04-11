N = int(input())
for i in range(1, N + 1):	
	valor = list(map(float, input().split()))	
	print ("A média {}: {}." .format (i, ((valor[0] * 2) + (valor[1] * 3) + (valor[2] * 5) / 10)))
