quantidade = int(input("Pizzas pedidas: "))
valor = float(input("Valor da pizza: R$ "))
total = quantidade * valor; imposto = total * 0.08
print ("Total: R$ {:.2f}." .format (total + imposto))
