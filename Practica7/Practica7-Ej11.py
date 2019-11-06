#Cristian Vigara Espinosa
#Pedir una frase y decir si es palindroma
print("Pedir una frase y decir si es palíndroma o no")
frase=input("Dime algo bonito: ")
def palin(x):
    y=x[::-1]
    if x==y:
        palin="%s es palíndroma"%(x)
    else:
        palin=x
    return palin
palin=palin(frase)
print(palin)