#Cristian Vigara Espinosa
#Calcular el precio con IVA
print("Calcular el precio con IVA")
precio=float(input("Introduzca el precio de su producto:"))
prod=input("¿De qué producto se trata?:")
iva=precio+(precio*0.21)
print("Tu",prod,"vale",precio,"euros y con el 21% de IVA se queda en ",iva,"euros en total")
input("Presiona ENTER para cerrar el programa")
