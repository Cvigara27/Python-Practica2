#Cristian Vigara Espinosa
#Definir un límite y pedir números hasta que la suma de estos sea igual al límite
print("Definir un límite y pedir números hasta que la suma de estos sea igual al límite")
limite=int(input("Establezca el límite:"))
num2=int(input("Escriba un valor:"))
lista=[num2]
total=num2
while limite!=total:
    if total>limite:
        lista.pop()
        total-=num2
        num2=int(input("El valor supera el límite, escriba otro número:"))
        lista.append(num2)
        total+=num2
    elif total<limite:
        num2=int(input("Escriba otro valor:"))
        total+=num2
        lista.append(num2)
print("El límite %d ha sido igualado por los números:"%(limite))
for i in lista:
    print(i,end=", ")
input("Presione ENTER para cerrar el programa")
