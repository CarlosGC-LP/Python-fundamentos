#Crearemos la super clase Animal, con el encabezado de una función o métodos pero sin su cuerpo, similar a las interfaces en java
class Animal:
    def comunicarse(self):
        raise NotImplementedError('La subclase debe implementar el' ' metodo comunicarse()')
#Crearemos las subclases que heredarán el método comunicarse pero deben implementar su código adaptado según sus necesidades, es decir hará polimorfismo
class Perro(Animal):
    def comunicarse(self):
        return 'Soy un perro y ladro, Guauuu!!!'
class Gato(Animal):
    def comunicarse(self):
        return 'Soy un gato y maullo, Miauuu!!!'
class Oso(Animal):
    def comunicarse(self):
        return 'Soy un oso y gruño, GGrrrrr!!!'
#Como tenemos varios objetos con métodos comunes, podemos meterlos en una lista
animales = [Perro(), Gato(), Oso()]

#Vamos a recorrer la lista
for animal in animales:
    print(animal.comunicarse())