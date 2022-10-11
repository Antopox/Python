from asyncio.windows_events import NULL
from email.errors import MessageError
from socket import MsgFlag
from tokenize import String

COD_articulos = []
nombre_art = {}
descripcion_art = {}
precio_art = {}

def buscarCOD(COD_art):
    if COD_art in COD_articulos:
        return 0  
    else:
        return 1
    
def comprobarCOD(COD_art):
    if 0 < COD_art <= 999999:
        return 1
    else:
        print("Codigo de producto inválido")
        return 0
    
def comprobarNombre(nombre):
    if nombre is not NULL:
        return 1
    else:
        print("Nombre inválido")
        return 0
    
def comprobarDescrip(descripcion):
    if descripcion is not NULL:
        return 1
    else:
        print("Descripción inválida")
        return 0
        
def comprobarPrecio(precio):
    if precio is not NULL:
        return 1
    else:
        print("Precio inválido")
        return 0

def alta(COD_art, nombre, descripcion, precio):
    correcto = buscarCOD(COD_art) == comprobarCOD(COD_art) == comprobarNombre(nombre) == comprobarDescrip(descripcion) == comprobarPrecio(precio) == 1 
    
    if correcto:
        COD_articulos.append(COD_art)
        nombre_art[COD_art] = nombre
        descripcion_art[COD_art] = descripcion
        precio_art[COD_art] = precio
        print("Artículo añadido con éxito")
        

def baja(COD_art):
   
    if buscarCOD(COD_art) == 0:
        seguro = input("Seguro que quieres borrar(S/N): ")
        if seguro:
            COD_articulos.remove(COD_art)
            nombre_art.pop(COD_art)
            descripcion_art.pop(COD_art)
            precio_art.pop(COD_art)
        return 0
    else:
        return 1

def modificar(COD_art, nombre, descripcion, precio):
    if buscarCOD(COD_art) == 0:
        nombre_art[COD_art] = nombre
        descripcion_art[COD_art] = descripcion
        precio_art[COD_art] = precio
        
    else:
        print("No se ha encontrado articulo con ese precio")


def buscar(COD_art):
  
    if buscarCOD(COD_art) == 0:
        print("Código: " + str(COD_art))
        print("Nombre: " + str(nombre_art[COD_art]))
        print("Descripción: " +str(descripcion_art[COD_art]))
        print("Precio: " + str(precio_art[COD_art]))
        
    else:
        print("No hay ningún artículo con ese código")

def listado():
    
    for i in COD_articulos:
        buscar(i)
        print("\n----------------------\n" )

salir = True
while salir:
    print("""(1) Alta artículo.    
        (2) Baja artículo.
        (3) Modificar artículo.
        (4) Buscar artículo.
        (5) Listado de artículos.
        (6) Salir
             
             """)
    opcion = int(input("Introduzca su opción: "))
    
    if opcion == 1:
        Cod = int(input("Introduzca el codigo del nuevo articulo: "))
        nombre = input("Introduzca el nombre del nuevo articulo: ")
        descr = input("Ponle una descripción al nuevo producto: ")
        precio = float(input("Precio del nuevo producto: "))
        alta(Cod, nombre, descr, precio)
    elif opcion == 2:
        Cod = int(input("Introduzca el codigo del articulo a eliminar: "))
        baja(Cod)
    elif opcion == 3:
        Cod = int(input("Introduzca el codigo del articulo a modificar: "))
        nombre = input("Introduzca el nuevo nombre del articulo: ")
        descr = input("Ponle una nueva descripción al producto: ")
        precio = float(input("Actualiza el precio del producto: "))
        modificar(Cod, nombre, descr, precio)
    elif opcion == 4:
        Cod = int(input("Introduzca el codigo del articulo a buscar: "))
        buscar(Cod)
    elif opcion == 5:
        listado()
    elif opcion == 6:
        salir = False
    else:
        print("Opción inválida.")