#Cristian Vigara Espinosa
#Definir si una fecha es correcta
print("Definir si una fecha es correcta")
dia=int(input("Introduzca el dia del més:"))
mes=int(input("Introduzca el número del més:"))
año=int(input("Introduzca el año:"))
if (mes<1 or mes>12):
	print(dia,"/",mes,"/",año,"Fecha incorrecta")
elif (año<1):
	print(dia,"/",mes,"/",año,"Fecha incorrecta")
elif (mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12 and dia>0 and dia<32):
	print(dia,"/",mes,"/",año,"Fecha correcta")
elif (mes==2 and dia>0 and dia<29):
	print(dia,"/",mes,"/",año,"Fecha correcta")
elif (mes==4 or mes==6 or mes==9 or mes==11 and dia>0 and dia<31):
	print(dia,"/",mes,"/",año,"Fecha correcta")
else:
	print(dia,"/",mes,"/",año,"Fecha incorrecta")
input("Presiona ENTER para cerrar el programa")
