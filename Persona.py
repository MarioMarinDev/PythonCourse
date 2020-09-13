
import json, os, random

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def brincar(self):
        print(self.nombre + " salto!")

    def birthday(self):
        self.edad += 1
        print(self.nombre + " cumplio años, ahora tiene " + str(self.edad))

    def saludar(self, persona):
        print(self.nombre + " saludo a " + persona.nombre)

    def sumar_edades(self, persona):
        total = str(self.edad + persona.edad)
        print("Las edades de " + self.nombre + " y " + persona.nombre + " es igual a " + total)

persona_1 = Persona("Mario", 25)
persona_2 = Persona("Juan", 34)

persona_1.brincar()
persona_2.brincar()

persona_1.birthday()

persona_1.saludar(persona_2)
persona_1.sumar_edades(persona_2)
