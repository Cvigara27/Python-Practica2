#Cristian Vigara Espinosa
#Definir un límite y pedir números hasta que la suma de estos supere el límite
print("Definir un límite y pedir números hasta que la suma de estos supere el límite")
limite=int(input("Establezca el límite:"))
num2=float(input("Escriba un valor:"))
lista=[num2]
total=num2
while limite>total:
    num2=float(input("Escriba otro valor:"))
    lista.append(num2)
    total+=num2
print("El límite %d ha sido superado por los números:"%(limite))
for i in lista:
    print(i,end=", ")    
input("Presione ENTER para cerrar el programa")
