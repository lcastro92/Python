#Utilizamos import para traer funciones que se encuentren en la misma carpeta 
import k_funciones

#Ingresamos 2 numeros
print("Ingresá 2 números")
numa=input()
numb=input()

#Llamamos al módulo que importamos . nombre de la función
div=k_funciones.divisible(numa,numb)
print(div)

#En la carpeta modulos tenemos el archivo ejemploFuncion, con una función para ver si un número es par o no
#Para importar desde otra ruta, hacemos
import sys
sys.path.insert(0, 'tecnicasDeProgramacion/modulos/')
#Y luego podemos importar nuestro modulo
import ejemploFuncion

#Ingresamos 1 numero
print("Ingresa 1 numero")
numa=input()

#LLamamos a la función que está en el módulo ingresado
print(ejemploFuncion.esPar(numa))
