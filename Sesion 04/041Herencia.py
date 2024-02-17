#Crearemos una super clase llamada figura con un atributo color y un método dibujar

class Figura:
    def __init__(self, color):
        self.color = color
    def dibujar(self):
        print(f'Estamos dibujando una figura en color: {self.color}')
#Crearemos una subclase llamada Rectangulo que hereda de figura
class Rectangulo(Figura):
    def __init__(self, color, ancho, alto):
        super().__init__(color) #Viene de la superclase Figura
        self.ancho = ancho
        self.alto = alto
    def calcular_area(self):
        return self.alto * self.ancho
class Circulo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio
    def calcular_area(self):
        return 3.14 * (self.radio ** 2)
#Construiremos los objetos
miRectangulo = Rectangulo('Azul', 9, 17)
miCirculo = Circulo('Amarillo', 13)

#Usaremos los métodos de la clase Rectangulo
miRectangulo.dibujar()

print('La figura es de tipo rectangulo')
print('El color de la figura es:', miRectangulo.color)
print('El area del rectangulo es:', miRectangulo.calcular_area())

miCirculo.dibujar()
print('La figura es de tipo circulo')
print('El color de la figura es:', miCirculo.color)
print('El area del circulo es:', miCirculo.calcular_area())