ocurrencias = {}
frase = input("Introduce una frase: ")

for i in frase:
    if i in ocurrencias:
        ocurrencias[i] += 1
    else:
        ocurrencias.put(i, 1)

print (ocurrencias)
 