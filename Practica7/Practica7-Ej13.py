#Cristian Vigara Espinosa
#Pedir si se quiere averiguar si un número es primo o no con for o while
from time import time
print("Pedir si se quiere averiguar si un número es primo o no con for o while(True or False)")
print("1-Emplear FOR")
print("2-Emplear WHILE")
answer=int(input("¿Qué método desea emplear?(Número, por favor) "))
while answer>2 or answer<1:
    answer=int(input("Selecciona uno de los números de arriba, por favor: "))
num1=int(input("Introduzca un número:"))
def FOR(num2):
    x=True
    if num2==2:
        x=True
    else:
        for i in range(2,num2):
            if num2%i==0:
                x=False
    return x
def WHILE(num2):
    contar=2
    if num2==2 or num2==1:
        x=True
    else:
        while contar<num2:
            if num2%contar==0:
                x=False
                contar+=num2
            else:
                x=True
                contar+=1
    return x
if answer==1:
    start_time=time()
    print(FOR(num1))
    elapsed_time=time()-start_time
    print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
if answer==2:
    start_time=time()
    print(WHILE(num1))
    elapsed_time=time()-start_time
    print("Tiempo transcurrido: %.10f segundos." % elapsed_time)
input("Presione ENTER para cerrar el programa")