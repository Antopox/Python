nota=0
def error ():
	print("retrolo amix")
def acierto ():
	print("todo un capo que sos")


print ("Todo se deberá escribir en minúscula para evitar fallos innecesarios.\n")
input("Nombre: ")

print ("\n1. Esta está regalada, venga, ¿cuanto es 2x2?\n")

respuesta1= int(input("2 x 2 es : "))

if respuesta1 == 4:
	acierto()
	nota+=1
else:
	error()

print ("\n2. Venga subimos un poco el level, (pero tampoco mucho no te asustes), ¿que función tiene 'if' en Python?\n")
 
respuesta2= input("Se utiliza para presentar una : ")

if respuesta2 == "condición":
	acierto()
	nota+=1
else:
	error()
	
print ("\n\nNota Final: ",nota)
