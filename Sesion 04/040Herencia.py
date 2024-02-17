#Mostraremos como se comporta la herencia eb Python
#Crearemos la super clase, clase base. clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def comer(self):
        print(f'{self.nombre} esta comiendo')
#Crearemos la subclase, clase derivada o clase hija
class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    def ladrar(self):
        print(f'{self.nombre} es de la raza {self.raza} y esta ladrando')
#Crearemos el objeto de clase Perro
print('Crearemos el objeto miPerro, de clase Perro\n'
      'que hereda atributos de la super clase Animal\n'
      'su nombre es Simba, y su raza es Labrador\n')
mi_perro = Perro('Simba', 'Ladrador')
mi_perro.comer()
mi_perro.ladrar()