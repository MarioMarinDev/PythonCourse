
import json, os

ruta = "lista.json"
terminar = False
lista = []

if os.path.exists(ruta):
    f = open(ruta, "r")
    lista = json.loads(f.read())
    f.close()

while terminar == False:
    print("[1] Agreagar un elemento\n[2] Ver lista\n[3] Eliminar un elemento\n[0] Salir")
    opcion = int(input("Que quieres hacer? "))
    if opcion == 1:
        elemento = input("Escribe el nombre del elemento: ")
        lista.append(elemento)
    elif opcion == 2:
        for elemento in lista:
            print(elemento)
    elif opcion == 3:
        elemento = input("Escribe el nombre del elemento: ")
        if elemento in lista:
            lista.remove(elemento)
            print("El elemento " + elemento + " se elimino.")
        else:
            print("El elemento " + elemento + " no esta en la lista.")
    else:
        terminar = True

lista_json = json.dumps(lista)
f = open(ruta, "w")
f.write(lista_json)
f.close()
