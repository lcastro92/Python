listaPersonas=[]

persona={
    "Nombre":"Lucas",
    "Edad":"29",
    "Direccion":"Holmberg"
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


