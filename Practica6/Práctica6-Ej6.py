#Cristian Vigara Espinosa
#Pedir dos números y luego solo recibir los que esten entre ellos
print("Pedir dos números y luego solo recibir los que esten entre ellos")
num1=int(input("Introduzca un número:"))
num2=int(input("Introduzca un número mayor que %d:"%(num1)))
while num1>num2:
    num2=int(input("%d no es mayor que %d,vuelve a provar:"%(num2,num1)))
num3=int(input("Introduzca un número entre %d y %d:"%(num1,num2)))
lista=[]
while num1<num3 and num2>num3:
    lista.append(int(num3))
    num3=int(input("Introduzca un número entre %d y %d:"%(num1,num2)))
print("Los números introducidos entre %d y %d son:"%(num1,num2))
for i in lista:
    print(i,end=", ")
input("Presione ENTER para cerrar el programa")
