import turtle

class Poligono:
    def __init__(self, nombre, lados, largo=100, color="black", grosor=3):
        self.nombre = nombre
        self.lados = lados
        self.largo = largo
        self.color = color
        self.grosor = grosor

    def dibujar(self):
        turtle.color(self.color)
        turtle.pensize(self.grosor)
        for lado in range(self.lados):
            turtle.forward(self.largo)
            turtle.right(360 / self.lados)

class Cuadrado(Poligono):
    def __init__(self, largo=100, color="black", grosor=3):
        super().__init__("Cuadrado", 4, largo, color, grosor)

    def dibujar_lleno(self):
        turtle.begin_fill()
        super().dibujar()
        turtle.end_fill()


cuadrado_1 = Poligono("Cuadrado", 4)
cuadrado_2 = Cuadrado(color="Blue", grosor=5)

cuadrado_2.dibujar_lleno()

turtle.done()
