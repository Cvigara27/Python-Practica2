#Cristian Vigara Espinosa
#Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.
print("Se sumarán todos los valores entre los dos números")
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca un número mayor que %d:"%(num1)))
num2+=1
suma=0
for i in range(num1,num2):
    suma=i+suma
print("El total es %d"%(suma))
input("Presione ENTER para cerrar el programa")
