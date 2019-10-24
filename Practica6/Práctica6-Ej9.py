#Cristian Vigara Espinosa
#Pedir un nombre y su telefono
print("Pedir un nombre y su telefono,se acaba cuando en el nombre pone S")
nombre=input("Introduzca un nombre:")
num=int(input("Introduzca el número de %s:"%(nombre)))
persona="%s:%d"%(nombre,num)
lista=[]
while nombre!="S":
    lista.append(persona)
    nombre=input("Introduzca un nombre:")
    if nombre!="S":
        num=int(input("Introduzca el número de %s:"%(nombre)))
        persona="%s:%d"%(nombre,num)
print("Los datos de las persona son:")
for i in lista:
    print(i)
input("Presione ENTER para cerrar el programa")
