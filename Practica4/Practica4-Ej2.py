#Cristian Vigara Espinosa
#Determinar si es orden ascendente, descendente o desordenado
print("Determinar si es orden ascendente, descendente o desordenado")
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca otro número:"))
num3=int(input("Introduzca otra vez un número:"))
num4=int(input("Introduzca un numerito:"))
num5=int(input("Introduzca el último número:"))
if (num1>num2 and num2>num3 and num3>num4 and num4>num5):
	print("Están en orden descendiente")
elif (num1<num2 and num2<num3 and num3<num4 and num4<num5):
	print("Están en orden ascendente")
else:
	print("Están desordenados")
input("Presiona ENTER para cerrar el programa")
