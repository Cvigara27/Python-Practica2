#Cristian Vigara Espinosa
#Pedir unos números y solo pueden ir incrementando, se acabe cuando no se incrementa
print("Escribir una lista que solo se puede incrementar,se acaba cuando deja de serlo")
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca un número mayor que %d:"%(num1)))
lista=[num1]
while num1<num2:
    lista.append(num2)
    num1=num2
    num2=int(input("Introduzca un número mayor que %d:"%(num2)))
print("Los números escritos son:")
for i in lista:
	print(i,end=", ")
input("Presione ENTER para cerrar el programa")
