from Perro import Perro

a=Perro("Vito","Bretón","Marrón")
print(a.get_nombre()+" es de raza: "+a.get_raza())
a.ladrar()

b=Perro("Lola","Yorkshire","Negro")
print(b.get_nombre()+" es de raza: "+b.get_raza())
b.ladrar()