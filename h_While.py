#El while es un bucle que nos permite repetir código en caso de que se cumpla determinada condición
#Por ejemplo mientras se ingrese un número negativo, seguirá pidiendo números

print("Ingresá un número")
num=input()

while int(num)<0:
    print("Ingresá un número positivo para terminar")
    num=input()
