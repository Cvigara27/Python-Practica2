#Cristian Vigara Espinosa
#Pedir un número y entregar todos sus divisores
num1=int(input("Introduzca un número:"))
print("Los dvisores de %d son:"%(num1))
for i in range(1,num1+1):
    if num1%i==0:
        print(i)
input("Presione ENTER para cerrar el programa")
