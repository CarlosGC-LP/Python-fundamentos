#Crearemos una clase que manipula información de vahiculos
#Usaremos un método para imprimir su ficha tecnica

class Vehiculo:
    def __init__(self, marca, tipo, modelo, color):
        self.marca = marca
        self.tipo = tipo
        self.modelo = modelo
        self.color = color
    def ficha_tecnica(self):
        print('\n----FICHA TECNICA DEL VEHICULO----\n')
        print('La marca del coche es:', self.marca)
        print('El tipo del coche es:', self.tipo)
        print('El modelo del coche es:', self.modelo)
        print('El color del coche es:', self.color)
#Crearemos nuestro primer objeto de clase Vehiculo
vehiculo = Vehiculo('Toyota', 'Tacoma', '2024', 'Blanco')

#Llamar al método ficha técnica
vehiculo.ficha_tecnica()
vehiculo.color = 'Rojo'
vehiculo.ficha_tecnica()