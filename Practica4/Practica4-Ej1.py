#Critian Vigara Espinosa
#Definir que número es mayor y cual es menor
print("Definir que número es mayor y cual es menor")
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca otro número:"))
num3=int(input("Introduzca otra vez un número:"))
num4=int(input("Introduzca un numerito:"))
num5=int(input("Introduzca el último número:"))
mayor=num1
menor=num1
if (num2>mayor):
	mayor=num2
if (num3>mayor):
	mayor=num3
if (num4>mayor):
	mayor=num4
if (num5>mayor):
	mayor=num5
if (num2<menor):
	menor=num2
if (num3<menor):
	menor=num3
if (num4<menor):
	menor=num4
if (num5<menor):
	menor=num5
print("El número mayor es",mayor,"y el número menor es",menor)
input("Presiona ENTER para cerrar el programa")
