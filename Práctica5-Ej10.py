#Cristian Vigara Espinosa
#Pedir la altura para dibujar una piramide
altura=int(input("Introduzca la altura:"))
espacio=" "*(altura-1)
for i in range(1,altura+1):
    dibujo="*"*i
    dibujo2="*"*(i-1)
    espacio=" "*(altura-i)
    if i==1:
        print(espacio,dibujo,espacio)
    else:
        print(espacio,dibujo+dibujo2,espacio)
input("Presione ENTER para cerrar el programa")
    
    
