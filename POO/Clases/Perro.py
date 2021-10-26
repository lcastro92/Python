#Podemos definir una clase Perro
class Perro:

#Sus atributos serán raza y color
    def __init__(self, nombre, raza, color):
        self.set_nombre(nombre)
        self.set_raza(raza) 
        self.set_color(color) 
    
    def set_nombre(self,nombre):
        self._nombre=nombre

    def get_nombre(self):
        return self._nombre

    def set_raza(self, raza):     
        self._raza = raza
    
    def get_raza(self):
        return self._raza

    def set_color(self,color):
        self._color=color

    def get_color(self, color):
        return self._color

    def ladrar(self):
        print("Guau guau!")
