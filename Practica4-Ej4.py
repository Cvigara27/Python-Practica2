#Cristian Vigara Espinosa
#Determinar si el cuarto número es divisor del los 3 primeros
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca otro número:"))
num3=int(input("Introduzca otra vez un número:"))
num4=int(input("Introduzca el último número:"))
if (num1%num4==0 and num2%num4==0 and num3%num4==0):
	print(num4,"es divisor de",num1,num2,num3)
input("Presiona ENTER para cerrar el programa")
