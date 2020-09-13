import json, os

diccionario = {
    "Nombre": "Mario",
    "Edad": 25,
    "Hobbies": ["Musica", "Juegos", "Cocinar"]
}
dict_json = json.dumps(diccionario, indent=2)

f = open("my_data.json", "w")
f.write(dict_json)
f.close()

# Leer la informacion
f = open("my_data.json", "r")
my_data = json.loads(f.read())
f.close()

print(my_data["Nombre"])

# Eliminar el archivo
if os.path.exists("my_data.json"):
    os.remove("my_data.json")
    print("El archivo se elimino")
else:
    print("El archivo no existe")
