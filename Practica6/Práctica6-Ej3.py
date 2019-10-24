#Cristian Vigara Espinosa
#Introducir números y guardarlas en un lista
print("Introducir palabras y guardarlas en un lista,introduzca un valor superior a 10 para salir")
x=float(input("Introduzca un número entre 0 y 10:"))
lista=[]
while x>=0 and x<=10:
    lista.append(x)
    x=""
    x=float(input("Introduzca más números:"))
print("Los números que has escrito son",lista)
input("Presione ENTER para cerrar el programa")
