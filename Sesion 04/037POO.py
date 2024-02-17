#Creamos la clase Persona

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f'Hola, mi nombre es: {self.nombre} y mi edad es: {self.edad}')
#Crearemos los objetos de la clase Persona
persona1 = Persona('Juan', 25)
persona2 = Persona('Ana', 31)

print('Se construyeron 2 objetos: persona1 y persona2\n')

#Accederemos a los atributos de estos objetos
print('El nombre de la persona1 es:', persona1.nombre)
print('La edad de la persona1 es:', persona1.edad)

print(f'\nEl nombre de la persona2 es: {persona2.nombre}', 
      f'\nLa edad de la persona2 es: {persona2.edad}')

#Accederemos a los métodos de los objetos
print('')
persona1.saludar()
persona2.saludar()