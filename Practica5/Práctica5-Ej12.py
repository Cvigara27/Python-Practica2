#Cristian Vigara Espinosa
#Pedir un número y decir si es primo o no
num1=int(input("Introduzca un número:"))
x=("El número %d es primo"%(num1))
if num1==2:
    print("El número %d es primo"%(num1))
else:
    for i in range(2,num1):
        if num1%i==0:
            x=("El número %d no es primo"%(num1))
print(x)
input("Presione ENTER para cerrar el programa")
