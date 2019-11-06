#Cristian Vigara Espinosa
#Pedir una cadena y cambiar todas las vocales por una demandada
print("Pedir una cadena y cambiar todas las vocales por una demandada")
cadena=input("Introduzca una cadena:")
vocal=input("¿Qué vocal quieres?:")
def cambio(chain):
    cadena2=chain.replace("a",vocal)
    cadena2=cadena2.replace("e",vocal)
    cadena2=cadena2.replace("i",vocal)
    cadena2=cadena2.replace("o",vocal)
    cadena2=cadena2.replace("u",vocal)
    return cadena2
cadena=cambio(cadena)
print(cadena)