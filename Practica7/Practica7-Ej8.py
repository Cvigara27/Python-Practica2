#Cristian Vigara Espinosa
#Compactar una frase, quitarle los espacios
print("Compactar una frase, quitarle los espacios")
frase=input("Introduzca una frase:")
def compactar(phrase):
    compact=phrase.replace(" ","")
    return compact
compacto=compactar(frase)
print(compacto)