#Cristian Vigara Espinosa
#Emplear diccionarios y pedir fecha formato dd/mm/yyyy y devolver la fecha con el nombre del mes
print("Emplear diccionarios y pedir fecha formato dd/mm/yyyy y devolver la fecha con el nombre del mes")
dicc={  "1":"Enero","2":"Febrero","3":"Marzo",
        "4":"Abril","5":"Mayo","6":"Junio","7":"Julio",
        "8":"Agosto","9":"Septimebre","10":"Octubre",
        "11":"Noviembre","12":"Diciembre"}
fecha=input("Introduzca un fecha: ")
fecha2=fecha.split("/")
print("%s de %s del %s"%(fecha2[0],dicc[fecha2[1]],fecha2[2]))