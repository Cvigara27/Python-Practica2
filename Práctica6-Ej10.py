#Cristian Vigara Espinosa
#Pedir un nombre y sus notas
print("Pedir un nombre y sus notas,se acaba cuando en el nombre pone una nota fuera del intervalo de 0-10 y no se pone nombre en el siguiente")
nombre=input("Introduzca un nombre:")
nota=float(input("Introduzca una nota de %s:"%(nombre)))
lista=[nombre]
lista2=[]
while nombre!="":
    if nota<0 or nota>10:
        nombre=input("Introduzca otro nombre:")
        if nombre!="":
            lista.append(nombre)
            nota=1
    if nombre!="":
        while nota>=0 and nota<=10 or nota=="":
            nota=float(input("Introduzca una nota de %s:"%(nombre)))
            if nota>=0 and nota<=10:
                 lista.append(nota)
            else:
                lista2.append([lista])
                lista=[]
for i in lista2:
    for i in i:
        print("Las notas de",i)
input("Presione ENTER para cerrar el programa")
