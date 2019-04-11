diario = int(input("Cigarros por dia: ")) * 10
anual = int(input("Quanto dias: ")) * 365
diasPerdidos = (diario * anual) / (60 * 24)
horasPerdidas = ((diario * anual) % (60 * 24)) / 60
minutosPerdidos = ((diario * anual) % (60 * 24)) % 60
print ("{} dia(s), {}  hora(s) e {} minuto(s)." .format(int(diasPerdidos), int(horasPerdidas), int(minutosPerdidos)))
