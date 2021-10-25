
class Perro:

    def __init__ (self, raza,nombre):
        self.raza=raza
        self.nombre=nombre

    def ladrar(cls):
        print("guagua")

diana  = Perro("yorkshire","Diana")

diana.ladrar()
