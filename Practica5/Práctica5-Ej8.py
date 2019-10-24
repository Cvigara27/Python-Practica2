#Cristian Vigara Espinosa
#Mediante una altura dibujar un triangulo
altura=int(input("Introduzca la altura del triangulo:"))
for i in range(1,altura+1):
    dibujo="*"*i
    print(dibujo)
for i in range(altura-1,0,-1):
    dibujo="*"*i
    print(dibujo)
input("Presione ENTER para cerrar el programa")
