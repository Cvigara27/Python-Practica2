#Cristian Vigara Espinosa
#Pedir un número y decir si es primo o no
print("Pedir un número y decir si es primo o no")
num1=int(input("Introduzca un número:"))
contar=2
if num1==2 or num1==1:
    x="El número %d es primo"%(num1)
else:
    while contar<num1:
        if num1%contar==0:
            x=("El número %d no es primo"%(num1))
            contar+=num1
        else:
            x="El número %d es primo"%(num1)
            contar+=1
print(x)
input("Presione ENTER para cerrar el programa")