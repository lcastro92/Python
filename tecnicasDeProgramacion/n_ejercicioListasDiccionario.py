listaPersonas=[]
#Los diccionarios son mapas de valores. Se declaran con {} 


persona={
    "Nombre":"Lucas", #primer elemento
    "Edad":"29",        #segundo elemento
    "Direccion":"Holmberg" #tercer elemento
}

listaPersonas.append(persona)
print(listaPersonas)

persona={
    "Nombre":"Maria",
    "Edad":"40",
    "Direccion":"ASdfgh"
}
listaPersonas.append(persona)
for persona in listaPersonas :   
    print (persona)

for persona in listaPersonas:
    if persona["Nombre"]=="Maria":
        persona.update({"Nombre":"Jorge"})

print (listaPersonas)


