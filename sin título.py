numero1 = 0
numero2 = 0
resultado = 0
print('¡Hola! Bienvenido a tu calculadora personal.\n¿En que puedo ayudarte?')
inicio = input("\nEscribe inicio para comenzar.   ")
while inicio != "inicio":
    print("\n ¡No entiendo que me quieres decir!🙄 \npara comenzar escribe 'inicio'")
    inicio = input("\nEscribe inicio para comenzar.   ")   
while inicio == "inicio":
    print("""¿Que operación desea realizar? Elige una opción:
    
     1 - Suma.
     2 - Resta.
     3 - Multiplicación.
     4 - División.
     5 - Exponente.
    
    Si quiere terminar puede poner lo que quiera excepto los comandos para realizar las operaciones(obviamente jeje)😅""")
    opcion = input()
    if opcion == '1':
        numero1 = input("Primer sumando: ")
        if numero1 == "ans":
            numero1 = resultado
        else:
            numero1 = float(numero1)
        numero2 = input("Segundo sumando: ")
        if numero2 == 'ans':
            numero2 = resultado
        else:
            numero2= float(numero2)
        resultado = numero1 + numero2
        print("el resultado es:   ","👉  ",resultado,"  👈")
    elif opcion == '2':
        numero1 = input("Minuendo: ")
        if numero1 == "ans":
            numero1 = resultado
        else:
            numero1 = float(numero1)
        numero2 = input("Sustraendo: ")
        if numero2 == 'ans':
            numero2 = resultado
        else:
            numero2= float(numero2)
        resultado = numero1 - numero2
        print("el resultado es:   ","👉  ",resultado,"  👈")
    elif opcion == '3':
        numero1 = input("Primer factor: ")
        if numero1 == 'ans':
            numero1 = resultado
        else:
            numero1 = float(numero1)
        numero2 = input("Segundo factor: ")
        if numero2 == 'ans':
            numero2 = resultado
        else:
            numero2= float(numero2)
        resultado = numero1 * numero2
        print("el resultado es:   ","👉  ",resultado,"  👈")
    elif opcion == '4':
        numero1 = input("Dividendo: ")
        if numero1 == 'ans':
            numero1 = resultado
        else:
            numero1 = float(numero1)
        numero2 = input("Divisor: ")
        if numero2 == 'ans':
            numero2 = resultado
        else:
            numero2= float(numero2)
        resultado = numero1 / numero2
        print("el resultado es:   ","👉  ",resultado,"  👈")
    elif opcion == '5':
        numero1 = input("Base: ")
        if numero1 == 'ans':
            numero1 = resultado
        else:
            numero1 = float(numero1)
        numero2 = input("Exponente: ")
        if numero2 == 'ans':
            numero2 = resultado
        else:
            numero2= float(numero2)
        resultado = numero1 ** numero2
        print("el resultado es:   ","👉  ",resultado,"  👈")
    else:
        print("\n Me alegra haber sido de ayuda. ¡Espero que vuelvas pronto!")
        break
