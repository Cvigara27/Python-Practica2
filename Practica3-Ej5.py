#Cristian Vigara Espinosa
#Pedir un numero de máximo 3 cifras
print("El númerp no puede ser mayor de 3 cifras")
num=int(input("Por favor introduzca un número:"))
if (num>999):
	print("ERROR:El número",num,"tiene más de tres cifras")
else:	
	print(num,"es un número valido")
input("Presiona ENTER para cerrar el programa")
