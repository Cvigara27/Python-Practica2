#Cristian Vigara Espinosa
#Pedir si calcular área de triangulo o cuadrado
print("Calcular el área de un triangulo o un cuadrado")
print("1.Cuadrado")
print("2.Triángulo")
num=float(input("Introduzca el número de la figura que se debe calcular el área:"))
if (num==1):
	lado=float(input("Introduzca la longitud del lado:"))
	area=lado*lado
	print("El área del cuadrado es:",area)
if (num==2):
	base=float(input("Introduzca la longitud de la base:"))
	altura=float(input("Introduzca la longitud de la altura:"))
	area=(base*altura)//2
	print("El área del triángulo es:",area)
input("Presiona ENTER para cerrar el programa")
	
