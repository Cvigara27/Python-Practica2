#Cristian Vigara Espinosa
#Dibujar una forma cuadrilátera según los datos proporcionados
altura=int(input("Introduzca la altura:"))
ancho=int(input("Introduzca la anchura:"))
dibujo="*"*ancho
for i in range(1,altura+1):
    print(dibujo)
input("Presione ENTER para cerrar el programa")
