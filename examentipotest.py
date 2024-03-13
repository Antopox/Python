respuestas= []
nota = 0
print ('''1.- ¿Qué dice el teorema de Pitágoras?
a- C^2 + C^2 = H^2
b- C + C = H
c- Ambas.''')
respuestas.append (input("Solución 1: "))

print ('''\n2.- ¿Que rey visigodo hizo la conversión del reino en católico?
a- Leovigildo.
b- Recadero.
c- Recesvinto.''')
respuestas.append (input("Solución 2: "))

print ('''\n3.- Nombre dado a España por los romanos.
a- Hispania.
b- Tarraconensis.
c- Espania.''')
respuestas.append (input("Solución 3: "))

print ('''\n4.- ¿Qué es una bisectriz?
a- Recta perpendicular que pasa por el punto medio de un segmento.
b- Recta empleada para hacer el Teorema de Tales.
c- Recta que corta un ángulo por la mitad.''')
respuestas.append (input("Solución 4: "))

print ('''\n5.- ¿Como podemos crear un bucle en Python?
a- while.
b- ambas.
c- for.''')
respuestas.append (input("Solución 5: "))

if respuestas[0] == "a":
	nota+=1
if respuestas[1] == "b":
	nota+=1
if respuestas[2] == "a":
	nota+=1
if respuestas[3] == "c":
	nota+=1
if respuestas[4] == "b":
	nota+=1
	
print ("\n\nTu nota final es!!: ",nota,"/5")

if nota == 5:
	print ("\n¡¡Felicidades,Tienes una puntuación perfecta!!")
