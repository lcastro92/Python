#Las funciones nos sirven para reutilizar código

def divisible(a, b):
    if int(a)%int(b)==0:
        return "Es divisible",5
    else:
       return "No es divisible"


print("Ingresa 2 valores")
valor1=input()
valor2=input()

print("Los valores ingresados son "+str(valor1)+" y "+str(valor2))
soloDiosSabra=divisible(valor1,valor2)
print (soloDiosSabra)


