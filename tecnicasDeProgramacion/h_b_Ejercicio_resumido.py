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


while compra!="0":
    if compra=="1":
        print("Eligió Micro")
        cant_micro+=1
        subtotal=subtotal+micro
    elif compra=="2":
        print("Eligió Rams")
        cant_ram+=1
        subtotal=subtotal+ram
    elif compra=="3":
        print("Eligió Teclado")
        cant_teclado+=1
        subtotal=subtotal+teclado
    elif compra=="4":
        print("Eligió Mouse")
        cant_mouse+=1
        subtotal=subtotal+mouse
    elif compra=="5":
        print("Eligió Mother")
        cant_mother+=1
        subtotal=subtotal+mother
    elif compra=="6":
        print("Eligió Fuente:")
        cant_fuente+=1
        subtotal=subtotal+fuente
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
    total=total - (subtotal*0.1) #Al total le saco el 10% del subtotal
if cant_micro>0 and cant_ram>0 and cant_teclado>0 and cant_mouse>0 and cant_mother>0 and cant_fuente>0: #Si todos los contadores tienen algún ítem
    total=total- (subtotal*0.1) #Al total le saco el 10% del subtotal
if cant_ram>=3: #Si compró más de 3 rams
   total = total - (cant_ram//3)*ram  #al total le saco las rams sobrantes

#Muestro total
print("El total es: "+str(total))
