"""
    open("Nombre del archivo.txt/json/ini", "modo")
    modos:
        r = Read; Leer el archivo ; Si no existe marca error
        w = Write; Escribir en el archivo (sobreescribir)
        a = Append; Escribir en el archivo (Sin modificarlo)
        x = Create; Si si existe el archivo marcará error

    funciones de variable f:
        close() # Cierra el archivo que abrí
        read()
        readline()
        readlines()
        write("lo que quiera escribir")
"""

f = open("prueba_01.txt", "r")
lineas = []
print(lineas)
# f.write("Este texto lo escribí desde Python3!")
f.close()