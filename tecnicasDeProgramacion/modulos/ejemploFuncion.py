#Vamos a definir una función para determinar si un número es par o no
def esPar(num):
    if int(num) %2 == 0:
        return "Par"
    else: 
        return "Impar"

'''
>>>esPar(2)
"Par"
'''
