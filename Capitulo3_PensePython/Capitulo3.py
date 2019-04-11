#ChamadaDeFunção

print (type(42))

print (int('32'))

print (int(3.99999))

print (int(-2.3))

print (float(32))

print (float('3.14159'))

print (str(32))

print (str(3.14159))

#FunçõesMatemáticas

import math

print (math)

signal_power = 10.0
noise_power = 15.5
ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
heigth = math.sin(radians)
degress = 45

print (heigth)

degrees = 45
radians = degrees / 180.0 * math.pi

print (math.sin(radians))

print (math.sqrt(2) / 2.0)

#Composição

x = math.sin(degrees / 360.0 * 2 * math.pi)

print (x)

x = math.exp(math.log(x+1))

print (x)

hours = 3
minutes = hours * 60

print (minutes)

#ComoAcrescentarNovasFunções

def print_lyrics():
	print ("I'm a lumberjack, and I'm okay.")
	print ("I sleep all night and I work all day.")

print (print_lyrics)

print (type(print_lyrics))

print (print_lyrics())

def repeat_lyrics():
	print_lyrics()
	print_lyrics()

print (repeat_lyrics())

#ParâmetrosEArgumentos

def print_twice(bruce):	
	print (bruce)
	print (bruce)

print (print_twice('Spam'))

print (print_twice(42))

print (print_twice(math.pi))

print (print_twice('Spam' * 4))

print (print_twice(math.cos(math.pi)))

michael = "Eric, the half a bee."

print (print_twice(michael))

#AsVariáveisEOsParâmetrosSãoLocais

def cat_twice(part1, part2):
	cat = part1 + part2
	print_twice(cat)

line1 = "Bing tiddle "
line2 = "tiddle bang."

print (cat_twice(line1, line2))


#FunçõesComResultadoEFunçõesNulas

x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

print (x)
print (golden)
print (math.sqrt(5))

result = print_twice("Bing")

print (result)

print (type(None))

