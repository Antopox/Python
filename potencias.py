#Funciones.
def po(n,p):
    for i in range(p):
        potencias.append(n**i)


#Variables.
n = int(input("numero: "))
p = int(input("numero de potencias: "))
potencias = []

#Código.
po(n,p)
print(potencias)