#no terminado

import os 

def limpiar_pantalla():
    if os.name=="nt":
        os.system("cls")
    else:
        os.system("clear")

def entrega_datos ():
    nombre= input("ingrese su nombre:")
    sueldo_base= float(input("ingrese su sueldo base:"))
    afp= input("ingrese ssu afp:")
    afp= afp.lower
    meses= int(input("ingrese la cantidad de meses que ah trabajado:"))
    hijos= int(input("ingrese la cantidad de hijos que tenga:"))

    return nombre,sueldo_base,afp,meses,hijos

def calcular_base_imponible(sueldo_base,hijos,meses):
    bonificacion_meses= sueldo_base*0.01*meses
    asignacion_familiar= sueldo_base*0.05*hijos
    base_imponible= sueldo_base*asignacion_familiar*bonificacion_meses
    
    return bonificacion_meses, asignacion_familiar, base_imponible

def fonasa(base_imponible):
    cotzacion_fonasa= base_imponible - 0.07
    
    return cotzacion_fonasa

def afp_seleccion(afp,base_imponible,cotizacion_fonasa):
    if afp=="felices":
        afp=base_imponible-0.12
    elif afp=="forrados":
        afp= base_imponible-0.114
    else:
        print("la afp ingresada es invalida")

    a_pagar= base_imponible-cotizacion_fonasa-afp

    return a_pagar
                
