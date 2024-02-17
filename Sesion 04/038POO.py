#Crearemos la clase Triangulo con un método para calcular su área
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
#Pediremos los datos necesarios para crear el objeto de clase Triangulo
base = float(input('Escribe la base del triangulo: '))
altura = float(input('Ahora escribe la altura del triangulo: '))

#Construiremos el objeto
triangulo = Triangulo(base, altura)

#Invocaremos el método para calcular el área
print('El area del triangulo es:', triangulo.area())