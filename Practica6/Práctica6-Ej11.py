#Cristian Vigara Espinosa
#El usuario debe adivinar un número generado aleatoriamente
print("El usuario debe adivinar un número generado aleatoriamente")
import random
import time
random.seed (time.time ())
minimo=int(input("Introduzca el valor mínimo:"))
maximo=int(input("Introduzca el valor máximo:"))
secreto = random.randint (minimo, maximo)
print("¿Puedes adivinar un número entre %d y %d?"%(minimo,maximo))
respuesta=int(input("Prueba un número:"))
contar=1
while respuesta!=secreto:
    contar+=1
    if respuesta<secreto:
        respuesta=int(input("¡Demasiado pequeño! Prueba otra vez:"))
    if respuesta>secreto:
        respuesta=int(input("¡Demasiado grande! prueba otra vez:"))
print("¡Correcto! Lo has intentado %d veces"%(contar))
input("Presiona ENTER para cerrar el programa")
