#Cristian Vigara Espinosa
#Introducir númer y guardarlas en un lista
print("Introducir números y guardarlas en un lista,introduzca Salir para terminar")
x=int(input("Introduzca un número:"))
lista=[]
while x!="Salir":
    lista.append(x)
    x=""
    x=input("Introduzca más números:")
print("Los números que has escrito son",lista)
input("Presione ENTER para cerrar el programa")
