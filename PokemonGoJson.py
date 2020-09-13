# ======== [ LIBRERIAS / PAQUETES ] ======== #
import random, json, os

# ======== [ FUNCIONES ] ======== #
# Regresar una lista con 5 pkmn del archivo db_pokemon.json
def buscar():
    f = open("db_pokemon.json", "r")
    pkmn_todos = json.loads(f.read())
    f.close()
    return random.sample(pkmn_todos, 5)

# Regresa True si se atrapó el Pokémon o de lo contrario, regresar False
def atrapar():
    return random.randint(1, 100) >= 50

# Regresa un diccionario con la información del Pokémon
# Obtiene el nombre del Pokémon como parametro
def generar_pokemon(nombre):
    nivel = random.randint(5, 100)
    return {
        "nombre": nombre,
        "nivel": nivel,
        "hp": random.randint(2, 5) * nivel
    }

# Regresa una lista del equipo del jugador
# Cargar la inforamción del archivo db_mis_pokemon.json
# Si el archivo no existe regresar una lista vacía []
def cargar_mi_equipo():
    if not os.path.exists("db_mis_pokemon.json"):
        return []
    f = open("db_mis_pokemon.json", "r")
    mi_equipo = json.loads(f.read())
    f.close()
    return mi_equipo

def guardar_mi_equipo(mi_equipo):
    f = open("db_mis_pokemon.json", "w")
    f.write(json.dumps(mi_equipo, indent=2))
    f.close()
    return

# ======== [ PROGRAMA PRINCIPAL ] ======== #
mi_equipo = cargar_mi_equipo()
terminar_juego = False

while terminar_juego == False:
    print("////// [ MENU ] //////")
    print("[1] Buscar Pokémon\n[2] Ver mis Pokémon\n[0] Guardar y salir")
    seleccion = int(input("¿Qué quieres hacer? "))
    if seleccion == 1:
        print("////// [ BUSCAR POKÉMON ] //////")
        pkmn_cerca = buscar()
        print("Encontraste estos Pokémon:")
        pkmn_index = 1
        for pkmn in pkmn_cerca:
            print("[{}] {}".format(pkmn_index, pkmn))
            pkmn_index += 1
        seleccion = int(input("¿Cuál quieres intentar capturar? ")) - 1
        print("////// [ RESULTADOS ] //////")
        if atrapar():
            pkmn_capturado = generar_pokemon(pkmn_cerca[seleccion])
            mi_equipo.append(pkmn_capturado)
            print("Capturaste un {} nivel {}".format(pkmn_capturado["nombre"], pkmn_capturado["nivel"]))
        else:
            print("{} logró escapar.".format(pkmn_cerca[seleccion]))
    elif seleccion == 2:
        print("////// [ MI EQUIPO ] //////")
        if len(mi_equipo) <= 0:
            print("No tienes Pokémon en tu equipo.")
            continue
        print("Estos son tus Pokémon:")
        pkmn_index = 1
        for pkmn in mi_equipo:
            print("[{}] {}".format(pkmn_index, pkmn["nombre"]))
            pkmn_index += 1
        seleccion = int(input("¿Cuál de tus Pokémon quieres ver? ")) - 1
        print("Nombre: " + mi_equipo[seleccion]["nombre"])
        print("Nivel: " + str(mi_equipo[seleccion]["nivel"]))
        print("HP: " + str(mi_equipo[seleccion]["hp"]))
    else:
        print("////// [ SALIENDO ] //////")
        guardar_mi_equipo(mi_equipo)
        terminar_juego = True
