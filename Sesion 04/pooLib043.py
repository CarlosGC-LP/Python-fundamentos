import pooLib042

class UsuariosPremium(pooLib042.Usuario):
    def __init__(self, id, alias, nombre, apellidos, sorteos, puntos):
        super().__init__(id, alias, nombre, apellidos)
        self.sorteos = sorteos
        self.puntos = puntos
    def muestra_datos(self):
        super().muestra_datos()
        print(f'Tienes {self.puntos} puntos para canjear en premios')
        print(f'Tienes derecho a participar en {self.sorteos} sorteos')
#Crearemos la instancia de un objeto de la clase UsuariosPremium
id = input('Introduce el ID del usuario: ')
alias = input('Escribe el Alias del usuario: ')
nombre = input('Escribe el nombre del usuario: ')
apellidos = input('Escribe los apellidos del usuario: ')

sorteos = 25 
puntos = 5000

userPremium = UsuariosPremium(id, alias, nombre, apellidos, sorteos, puntos)
userPremium.muestra_datos()