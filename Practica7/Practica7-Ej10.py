#Cristian Vigara Espinosa
#Decir si una palabra o número es palindromo o capicua
print("Decir si una palabra o número es palindromo o capicua")
cosa=input("Introduzca un número o palabra:")
def palin(x):
    y=x[::-1]
    if x==y:
        capi="Es un capicúa o palíndromo"
    else:
        capi="No es un capicúa o palíndromo"
    return capi
capi=palin(cosa)
print(capi)