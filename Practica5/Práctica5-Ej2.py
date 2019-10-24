#Cristian Vigara Espinosa
#Escribe un programa que pida dos números y
#escriba qué números entre ese par de números son pares y cuáles impares
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca un número mayor que %d:"%(num1)))
num2+=1
for i in range(num1,num2):
    if i%2==0:
        print("El número %d es par"%(i))
    else:
        print("El número %d es inpar"%(i))
input("Presione ENTER para cerrar el programa")
