#Cristian Vigara Espinosa
#Introducir dos valor y no termina hasta que el segundo sea mayor que el primero
print("Introduce 2 valores, hasta que el segundo no sea mayor que el primero no acaba")
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca un número mayor que %d:"%(num1)))
while num1>num2:
    num2=int(input("%d no es mayor que %d,vuelve a introducir un número:"%(num2,num1)))
print("Los números introducidos son %d y %d"%(num1,num2))
input("Presione ENTER para cerrar el programa")
