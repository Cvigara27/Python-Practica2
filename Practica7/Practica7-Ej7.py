#Cristian Vigara Espinosa
#Contar las vocales de una cadena
print("Contar las vocales de una cadena")
frase=input("Introduzca una frase:")
def contar(phrase):
    phrase=phrase.lower()
    a=phrase.count("a")+phrase.count("á")+phrase.count("à")
    e=phrase.count("e")+phrase.count("é")+phrase.count("è")
    i=phrase.count("i")+phrase.count("í")+phrase.count("ì")
    o=phrase.count("o")+phrase.count("ó")+phrase.count("ò")
    u=phrase.count("u")+phrase.count("ú")+phrase.count("ù")+phrase.count("ü")
    print("Se han encontrado %d A, %d E, %d I, %d O y %d U"%(a,e,i,o,u))
contar(frase)