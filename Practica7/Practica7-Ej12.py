#Cristian Vigara Espinosa
#Pedir una frase y contar el número de palabras
print("Pedir una frase y contar cuantas palabras hay")
frase=input("introduzca una frase: ")
def contar(x):
    x=x.replace(","," ")
    x=x.replace(";"," ")
    x=x.replace("."," ")
    x=x.replace(":"," ")
    x=x.replace("-"," ")
    x=x.replace("_"," ")
    x=len(x.split())
    return x
contar=contar(frase)
print("Hay %s palabras"%(contar))