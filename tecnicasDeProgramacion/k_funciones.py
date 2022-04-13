#Las funciones nos sirven para reutilizar código

def suma (a,b,c):
    total=float(a)+float(b)+float(c)
    print("La suma es "+str(total))

suma(1,4,3)

def saludo(nombre,apellido):
    print("Hola "+nombre+" "+apellido)

saludo("Lucas","Castro")
saludo("María", "Perez")
saludo("Juan", "Gomez")

def divisible(a, b):
    if int(a)%int(b)==0:
        return "Es divisible"
    else:
       return "No es divisible"


'''print("Ingresa 2 valores")
valor1=input()
valor2=input()

print("Los valores ingresados son "+str(valor1)+" y "+str(valor2))
print(divisible(valor1,valor2))
'''


def generar_usuario(nombre,apellido,edad):
    usuario=nombre[0]+nombre[1]+apellido[0]+apellido[1]+edad
    return usuario

print("Ingresá tu nombre, apellido y edad")
nombre=input()
apellido = input()
edad = input()

usuario=generar_usuario(nombre,apellido,edad)
print("Tu usuario es: "+usuario)