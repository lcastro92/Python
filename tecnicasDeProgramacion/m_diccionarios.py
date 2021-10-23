#Los diccionarios son mapas de valores. Se declaran con {} 
persona={
    'Nombre':"Lucas", #primer elemento
    'Edad':29,        #segundo elemento
    'Direccion':"Calle Falsa 455" #tercer elemento
}

print (persona)

#También se pueden declarar los valores de la siguiente manera:
persona={}
persona['Nombre']='Maria'
persona['Edad']=30
persona['Direccion']="Corrientes 123"

print(persona)

#Si queremos ver cada nombre de elemento, podemos hacer 
for valor in persona.keys():
    print(valor)

#Si queremos ver cada valor guardado, podemos hacer:
for valor in persona.values():
    print(valor)

#Para reemplazar valores dentro de cada diccionario, podemos hacer
persona['Direccion']="Cabildo 321"

print(persona)



