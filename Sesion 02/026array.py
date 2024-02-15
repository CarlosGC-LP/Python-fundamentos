numeros = [] #Arreglo vacio para guardar números

#Solicitar al usuario ingresar números
for i in range(5):
    numero = float(input('Ingresa el número: '))
    numeros.append(numero) #Agregar el numero al arreglo
#Calcular la suma de los números
suma = sum(numeros)

#Mostrar la suma de los números
print(' ')
print('La suma de los números es:', suma)