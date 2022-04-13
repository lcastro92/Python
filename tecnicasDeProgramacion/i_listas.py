#Las listas nos sirven para tener una colección de elementos, y poder acceder a ellos. 
# No hace falta que estén ordenados y pueden estar duplicados
colores=["Rojo","Amarillo","Azul"]

#Las listas pueden almacenar elementos de diferente tipo

componentes= [23.4,"Avión","Perro",123]
cont=0
for i in componentes:
    print("posición: "+str(cont)+" Valor: "+str(i))
    cont+=1

ultima_posicion=len(componentes)-1
print("Última posición: "+str(ultima_posicion))


print("Lista original: "+str(componentes))
componentes.append("Rompecabezas")
print("Lista nueva: "+str(componentes))

for items in componentes:
    print(items)

cantidad_valores=len(componentes)
print("Cantidad de valores: " +str(cantidad_valores))

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

listado=[]

contador_alumnos=0
for alumno in range(3):
    print("Alumno: "+str(contador_alumnos))
    contador_datos=0
    datos_alumno=[]
    for i in range(4):
        dato=input("Ingrese el dato "+str(contador_datos)+": ")
        datos_alumno.append(dato)
        contador_datos+=1
    listado.append(datos_alumno)
    contador_alumnos+=1
print(listado)
