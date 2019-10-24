#Cristian Vigara Espinosa+
#Pida al usuario un importe en euros y diga si el cajero automático 
#le puede dar dicho importe utilizando el mismo billete y el más grande
cantidad=int(input("Especifique la cantidad que desea sacar:"))
if (cantidad%500==0):
	billete=cantidad//500
	print("El cajero le devuelve",billete,"billete/s de 500")
elif (cantidad%200==0):
	billete=cantidad//200
	print("El cajero le devuelve",billete,"billete/s de 200")
elif (cantidad%100==0):
	billete=cantidad//100
	print("El cajero le devuelve",billete,"billete/s de 100")	
elif (cantidad%50==0):
	billete=cantidad//50
	print("El cajero le devuelve",billete,"billete/s de 50")
elif (cantidad%20==0):
	billete=cantidad//20
	print("El cajero le devuelve",billete,"billete/s de 20")
elif (cantidad%10==0):
	billete=cantidad//10
	print("El cajero le devuelve",billete,"billete/s de 10")
elif (cantidad%5==0):
	billete=cantidad//5
	print("El cajero le devuelve",billete,"billete/s de 5")
input("Presiona ENTER para cerrar el programa")
