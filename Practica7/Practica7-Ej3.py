#Cristian Vigara Espinosa
#Pedir una cadena e imprimirla un caracter por linea
print("Pedir una cadena e imprimirla un caracter por linea")
cadena=input("Introduzca una frase:")
def lineas(frase):
    for i in frase:
        print(i)
lineas(cadena)