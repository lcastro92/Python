from Perro import Perro
from Aritmetica import Aritmetica

a=Perro("Vito","Bretón","Marrón")
print(a.get_nombre()+" es de raza: "+a.get_raza())
a.ladrar()

b=Perro("Lola","Yorkshire","Negro")
print(b.get_nombre()+" es de raza: "+b.get_raza())
b.ladrar()

c=Aritmetica(5,4)
print("Suma: "+str(c.sumar()))
print(f'division: {c.dividir()}')