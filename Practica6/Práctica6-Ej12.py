#Cristian Vigara Espinosa
#El ordenador debe adivinar un número generado aleatoriamente
print("El ordenador debe adivinar un número generado aleatoriamente")
print("Se le dan pistas de igual/mayor/menor")
import random
import time
random.seed (time.time ())
minimo=int(input("Introduzca el valor mínimo:"))
maximo=int(input("Introduzca el valor máximo:"))
while minimo>maximo:
    maximo=int(input("¡ERROR! %d no es mayor que %d:"%(maximo,minimo)))
print("¿Debo adivinar un número entre %d y %d?"%(minimo,maximo))
guess=random.randint(minimo,maximo)
answer=input("¿Es %d el número secreto? "%(guess))
contar=1
while answer!="igual" and minimo<=maximo:
    contar+=1
    if answer=="menor" and minimo<maximo:
        maximo=guess-1
        guess=random.randint(minimo,maximo)
        answer=input("¿Es %d el número secreto? "%(guess))
    if answer=="mayor" and minimo<maximo:
        minimo=guess+1
        guess=random.randint(minimo,maximo)
        answer=input("¿Es %d el número secreto? "%(guess))
if answer=="igual":
    print("¡Soy un capo! Lo he conseguido en %d intentos"%(contar))
else:
    print("¡Sos un tramposo,Mi no querer jugar más!")
input("Presiona ENTER para cerrar el programa")
