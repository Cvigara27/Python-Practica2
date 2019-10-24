#Cristian Vigara Espinosa
#Dibujar un cuadrilatero sin relleno
altura=int(input("Introduzca la altura:"))
ancho=int(input("Introduzaca la anchura:"))
espacio=" "*(ancho-2)
for i in range(1, altura+1):
    dibujo="*"*ancho
    dibujo2="*%s*"%(espacio)
    if i==1:
        print(dibujo)
    elif i==altura:
        print(dibujo)
    else:
        print(dibujo2)  
input("Presione ENTER para cerrar el programa")
