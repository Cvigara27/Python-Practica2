#Cristian Vigara Espinosa
#Pedir un texto y devolverlo en mayuscula y minusculas
print("Pedir un texto y devolverlo en mayuscula y minusculas")
texto=input("Introduzca un texto:")
def cambio(texto2):
    print("En mayúsculas:",texto2.upper())
    print("En minúsculas:",texto2.lower())
cambio(texto)