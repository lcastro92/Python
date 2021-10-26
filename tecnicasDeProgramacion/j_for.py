#El bucle for nos sirve cuando sabemos la cantidad de veces que necesitamos repetir código.
#Por ejemplo para recorrer una lista o un String, en el que conocemos la cantidad de veces que hay que
#repetir el código (la longitud de la lista/string)
colores=["Rojo","Amarillo","Azul"]

#Para trabajar con la lista elemento a elemento usamos for
for color in colores:
    print(color)

 #para ver una lista al revés, usamos la función reversed()
for color in reversed(colores):
    print(color)


#También podemos usar un for para recorrer un String letra a letra
palabra = "Hola a todos"
for letra in palabra :   
    print(letra)

print(colores)

