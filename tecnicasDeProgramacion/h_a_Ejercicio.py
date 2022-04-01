print ("Ingrese que producto desea comprar: ")
print ("1.Micro 2.Ram 3.Teclado 4.Mouse 5.Mother 6.Fuente")
print("Para finalizar la compra ingrese '0'")
 
compra=input()
#################PRECIOS#######################
micro=1200
ram=800
teclado=300
mouse=200
mother=1300
fuente=1100
subtotal=0          #Subtotal
##############CONTADORES#######################
cant_micro=0
cant_ram=0
cant_teclado=0
cant_mouse=0
cant_mother=0
cant_fuente=0
#############DESCUENTOS#######################
dcto_4000_valor=0.10   #Descuento por total mayor a 4000
dcto_kit_completo_valor=0.10 #Descuento por comprar kit completo
dcto_4000=0             #Descuento de mayor a 4000 = 0, si hay descuento =1
dcto_kit_completo=0     #Descuento kit completo =0 , si hay descuento vale = 1
dcto_ram=0   #Descuento ram, si hay descuento vale =1 
dcto_ram_valor=0 #Total a descontar por el descuento de ram, si hay descuento vale cantidad de rams // 3 * precio de ram

while compra!="0":
    if compra=="1":
        print("Ingrese la cantidad de Micros:")
        cantidad=input() #Cantidad que desea comprar 
        cant_micro=cant_micro+int(cantidad) #cantida de micros compradas hasta el momento + las que elige comprar ahora
        subtotal=subtotal+micro*int(cantidad) #Subtotal actual + la cantidad de micros que desea comprar * el precio
    elif compra=="2":
        print("Ingrese la cantidad de Rams:")
        cantidad=input()
        cant_ram=cant_ram+int(cantidad)
        subtotal=subtotal+ram*int(cantidad)
    elif compra=="3":
        print("Ingrese la cantidad de Teclados:")
        cantidad=input()
        cant_teclado=cant_teclado+int(cantidad)
        subtotal=subtotal+teclado*int(cantidad)
    elif compra=="4":
        print("Ingrese la cantidad de Mouses:")
        cantidad=input()
        cant_mouse=cant_mouse+int(cantidad)
        subtotal=subtotal+mouse*int(cantidad)
    elif compra=="5":
        print("Ingrese la cantidad de Mothers:")
        cantidad=input()
        cant_mother=cant_mother+int(cantidad)
        subtotal=subtotal+mother*int(cantidad)
    elif compra=="6":
        print("Ingrese la cantidad de Fuentes:")
        cantidad=input()
        cant_fuente=cant_fuente+int(cantidad)
        subtotal=subtotal+fuente*int(cantidad)
    else:
        print("Metiste cualquiera pa, para salir 0") #Si pone algo que no va le avisa

    print ("Ingrese que producto desea comprar: ")
    print ("1=Micro 2=Ram 3=Teclado 4=Mouse Mother=5 Fuente=6")
    print("Para finalizar la compra ingrese '0'") 
    compra=input()   

####################### MUESTRO CONTADORES#################################
print("Total: ")
print("Micros: "+str(cant_micro))
print("Rams: "+str(cant_ram))
print("Teclado: "+str(cant_teclado))
print("Mouse: "+str(cant_mouse))
print("Mother: "+str(cant_mother))
print("Fuente: "+str(cant_fuente))


###################### CALCULO DESCUENTOS ##################################
total=subtotal #Me copio el subtotal, sobre esta variable haré los descuentos
if subtotal > 4000:
    dcto_4000=1   #Si el subtotal es mayor a 4000, hay descuento, entonces la variable de hay descuento = 1
    total=subtotal-total*(dcto_4000*dcto_4000_valor) # al total le resto el 10% del subtotal
if cant_micro>0 and cant_ram>0 and cant_teclado>0 and cant_mouse>0 and cant_mother>0 and cant_fuente>0: #Si todos los contadores tienen algún ítem
    dcto_kit_completo=1  #Hay descuento de kit completo, por eso vale =1
    total=total-subtotal*(dcto_4000*dcto_4000_valor) #al total le resto el 10% del subtotal
if cant_ram>=3: #Si compró más de 3 rams
    dcto_ram=1 #Hay descuento de rams
    dcto_ram_valor=(cant_ram//3)*ram #Calculo cuántas rams debo restarle al total
    total=total-dcto_ram*dcto_ram_valor #Al total le resto las rams de descuento


################################### MUESTRO SUBTOTAL; DESCUENTOS Y TOTAL ########################################
print("Subtotal "+str(subtotal))
print("Descuento por Precio Superior a 4000: "+str(subtotal*(dcto_4000*dcto_4000_valor)))
print("Descuento por Kit Completo: "+str(subtotal*(dcto_kit_completo*dcto_kit_completo_valor)))
print("Descuento por 3x2 en Rams: "+str(dcto_ram*dcto_ram_valor))
print("Total: "+str(total))
