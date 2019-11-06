#Cristian Vigara Espinosa
#Pedir una cadena y cambiar los espacios por *
print("Pedir una cadena y cambiar los espacios por *")
cadena=input("Introduzca una cadena con espacios:")
def espacios(chain):
    cadena2=chain.replace(" ","*")
    return cadena2
cadena=espacios(cadena)
print(cadena)