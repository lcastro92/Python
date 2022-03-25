class Aritmetica:
    
    def __init__(self, operandoA, operandoB):
        self.operandoA=operandoA
        self.operandoB=operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB