#Cristian Vigara Espinosa
#Pedir 3 cadenas y unirlas
print("Pedir 3 cadenas y unirlas")
nombre=input("Introduzca su nombre:")
apellido1=input("Introduzca su primer apellido:")
apellido2=input("Introduzca su segundo apellido:")
def unir(name,sur1,sur2):
    completo="Tu nombre es:%s %s %s"%(name,sur1,sur2)
    return completo
nombre=unir(nombre,apellido1,apellido2)
print(nombre)