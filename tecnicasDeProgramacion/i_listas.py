#Las listas nos sirven para tener una colección de elementos, y poder acceder a ellos. 
# No hace falta que estén ordenados y pueden estar duplicados

colores=["Rojo","Amarillo","Azul"]

#Para imprimir la lista
print(colores)

#podemos ver la longitud de la lista con len()
longitud=len(colores)
print(longitud)

#Podemos modificar los valores almacenados, por ejemplo para reemplazar el Rojo por Naranja se haría
colores[0]="Naranja"

print(colores)

#Podemos insertar valores con insert (recordar pasarle la posición)
colores.insert(1,"Rojo")
print (colores)

#Para agregar valores a la lista, usamos append()
colores.append("Violeta")
print(colores)

#También podemos agregarle a nuestra lista otra lista más
coloresNuevos=["Verde","Gris","Negro"]
colores.extend(coloresNuevos)
print(colores)

#Para borrar items de nuestra lista usamos .remove (Tener en cuenta que sólo borra el primero que coincide)
colores.remove("Verde")
print(colores)

#Si sabemos en que posición se encuentra el valor a borrar usamos pop
colores.pop(0)
print (colores)

#Tambien podemos usar la palabra reservada del
del colores[0]
print (colores)

#Para borrar todos los valores de nuestra lista usamos clear
colores.clear()
print (colores)


#Podemos buscar la posición en donde se encuentra un valor con index (usar if si no se sabe si está 
# o no el valor sino tira error)

#print(colores.index("Azul"))

#Para usarlo sin saber si está el color, usarlo con if

if "Morado" in colores:
    print(colores.index("Morado")) #No devuelve nada porque no existe el morado en la lista



