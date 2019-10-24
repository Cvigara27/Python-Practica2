#Cristian Vigara Espinosa
#Introducir palabras y guardarlas en un lista
print("Introducir palabras y guardarlas en un lista,presiona ENTER para terminar")
x=input("Introduzca una palabra:")
lista=[]
while x!="":
    lista.append(x)
    x=""
    x=input("Introduzca más palabras:")
print("Las palabras que has escrito son",lista)
input("Presione ENTER para cerrar el programa")
