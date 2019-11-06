#Cristian Vigara Espinosa
#Comprovar si dos palabra riman(Que acaban igual)
print("Comprovar si dos palabra riman(Que acaban igual)")
pal1=input("Introduzca la primera palabra:")
pal2=input("Introduzca la segunda palabra:")
def buscarimas(word1,word2):
    if word1[-3:]==word2[-3:]:
        print("Las palabras %s y %s riman "%(word1,word2))
    elif word1[-2:]==word2[-2:]:
        print("Las palabras %s y %s riman un poco"%(word1,word2))
    else:
        print("Las palabras %s y %s no riman"%(word1,word2))
buscarimas(pal1,pal2)