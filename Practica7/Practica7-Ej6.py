#Cristian Vigara Espinosa
#Buscar una lentra en una cadena
print("Buscar una lentra en una cadena")
cadena=input("Introduzca una frase:")
letra=input("¿Qué letra estas buscando?")
def buscador(chain,letter):
    i=0
    salir=False
    while i<len(chain) and salir==False:
        if cadena[i]==letra:
            encontrado="Se ha encontrado la letra %s en la posicion %d"%(letter,i)
            salir=True
        else:
            i+=1
            encontrado="No se ha encontrado tu letra"
    return encontrado
buscar=buscador(cadena,letra)
print(buscar)