#Cristian Vigara Espinosa
#Escribe un programa que pida un número y calcule su factorial.
num1=int(input("Introduzca un número:"))
factorial=1
for i in range(1,num1+1):
    factorial=factorial*i
print("El factorial de %d es:%d"%(num1,factorial))
input("Presione ENTER para cerrar el programa")

