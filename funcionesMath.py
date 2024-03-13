n1 = int(input("Introduce un dato: "))
n2 = int(input("Introduce otro dato: "))

def suma(n1, n2):
    resultado = (n1 + n2)
    return str(resultado)

def resta(n1, n2):
    resultado = (n1 - n2)
    return str(resultado)

def multiplicacion(n1, n2):
    resultado = (n1 * n2)
    return str(resultado)

def division(n1, n2):
    resultado = (n1 / n2)
    return str(resultado)

print(suma(n1, n2))
print(resta(n1, n2))
print(multiplicacion(n1, n2))
print(division(n1, n2))