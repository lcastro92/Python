#Para comparar usamos if, ejemplo de if para ver si alguien es mayor de edad o no
print("Ingrese su edad")
edad=input()

if int(edad)<18:
    print("Sos menor de edad")
elif int(edad)==18:
    print("Tenes 18")
else:
    print("Sos mayor de edad")