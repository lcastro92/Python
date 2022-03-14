#Existen diferentes tipos de datos que podemos almacenar
#Entre ellos, tenemos los int, floats y strings

años = 29 #este es un entero

dinero= 12.4 #Este es un float

nombre="Lucas" #Este es un string

#Sólo podemos imprimir Strings, por lo que para poder imprimir enteros (int) y decimales (floats) debemos 
#Transformarlos a Strings haciendo str()

print("Mi nombre es "+nombre+" tengo "+str(años)+" años y $"+str(dinero))

#También podemos transformar strings a enteros haciendo int() o a floats haciendo float()

sueldo = "12000"
sueldoNuevo= float(sueldo)
