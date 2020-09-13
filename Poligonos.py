import turtle

class Poligono:
    def __init__(self, lados, nombre, largo=100, color="black", grosor=3):
        self.lados = lados
        self.nombre = nombre
        self.largo = largo
        self.color = color
        self.grosor = grosor

    def dibujar(self):
        turtle.color(self.color)
        turtle.pensize(self.grosor)
        for i in range(self.lados):
            turtle.forward(self.largo)
            turtle.right(360 / self.lados)

class Cuadrado(Poligono):
    def __init__(self, largo=100, color="black", grosor=3):
        super().__init__(4, "cuadrado", largo, color, grosor)

class Hexagono(Poligono):
    def __init__(self, largo=100, color="black", grosor=3):
        super().__init__(6, "hexagono", largo, color, grosor)

    def dibujar(self):
        turtle.begin_fill()
        super().dibujar()
        turtle.end_fill()

# Poligonos Objeto
cuadrado = Poligono(4, "cuadrado", 150, "blue", 5)
pentagono = Poligono(5, "pentagono")
hexagono = Poligono(6, "haxagono", grosor=20, color="red")
icosagono = Poligono(20, "icosagono", 25)

# Poligonos Clase
cuadrado = Cuadrado(200, "red", 1)
hexagono = Hexagono(color="blue", grosor=5)

hexagono.dibujar()
turtle.done()