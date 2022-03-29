class Persona:
    #agregamos a init tuplas y diccionarios
    def __init__ (self, nombre,apellido,edad, *valores, **diccionario):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.valores=valores
        self.diccionario=diccionario

    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.diccionario}')


persona1 =Persona('Juan','Perez', 34 ,4,3,2, direccion='Calle falsa 1234', telefono='35456')
persona1.mostrar_detalle()

persona2 =Persona('Maria','Gomez', 50 )
persona2.mostrar_detalle()