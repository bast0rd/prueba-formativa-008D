import time
import os
import csv


trabajadores = []
bl = "─"*36
n = 0
cargos = ("CEO", "Desarrollador", "Analista de datos", "diseñador grafico", "tester")
contador = True 
error = "error en la opcion."
descuento_salud = 70000
descuento_AFP = 120000

archivo = 'trabajadores.txt'

if os.path.exists(archivo):
    os.system("cls")
else:
    sistema = ("Trabajador", "Cargo", "Sueldo Bruto", "Desc. Salud", "Desc. AFP", "Líquido a pagar")
    sistema_str = "      ".join(sistema)
    os.system("cls")
    with open('trabajadores.txt','w') as archivo:
        archivo.write(sistema_str + '\n')
    
def borrar(b):
    time.sleep(b)
    os.system("cls")
    
def menu():
    global contador
    while contador == True:
        print(f"menu del trabajador \n{bl}")
        print(f"1) agregar trabajador \n2) imprimir plantilla de sueldo \n3) salir")
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print(error)
            borrar(1)
            continue
        if eleguir in [1,2,3]:
            borrar(0.5)
            return(eleguir)
        else:
            print("no es una opcion")
            borrar(1)
            
def trabajador():
    global contador
    while contador == True:
        print(f"escriba el nombre del trabajador \n{bl}")
        trabajador_nombre_ing = input("──> ")
        trabajador_Apellido_ing = input("ahora ingrese su apellido \n──> ")
        trabajador_ing = trabajador_nombre_ing + " " + trabajador_Apellido_ing
        borrar(0.5)
        while contador == True:
            print(f"estas seguro que deseas agregar este nombre? ──> {trabajador_ing} (s/n)\n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                trabajadores.append(trabajador_ing)
                borrar(0.5)
                contador = False
            elif eleguir in ["n", "N"]:
                borrar(0.5)
                break
            else:
                print("no es una opcion")
                borrar(1)
    contador = True
            
def cargo():
    global n, contador
    while contador == True:
        n = 0
        print(f"selecione un cargo \n{bl}")
        for i in cargos:
            n += 1
            print(f"{n}) {i}")
            time.sleep(0.1)
        try:
            eleguir = int(input("──> "))
        except ValueError:
            print(error)
            borrar(1)
            continue
        if eleguir in [1,2,3,4,5]:
            eleguir -= 1
            trabajadores.append(cargos[eleguir])
            break
        else:
            print("no es una opcion")
            borrar(1)
            
def sueldos():
    global contador
    while contador == True:
        print(f"ingrese el sueldo del trabajador \n{bl}")
        try:
            sueldo = float(input("──> "))
        except ValueError:
            print(error)
            borrar(1)
            continue
        while contador == True:
            print(f"esta bien el sueldo ingresado? ──> {sueldo} (s/n) \n{bl}")
            eleguir = input("──> ")
            if eleguir in ["s","S"]:
                sueldo_str = str(sueldo)
                trabajadores.append(sueldo_str)
                borrar(0.5)
                contador = False
            elif eleguir in ["n", "N"]:
                borrar(0.5)
                break
    contador = True
    descuento_salud_str = str(descuento_salud)
    descuento_AFP_str = str(descuento_AFP)
    trabajadores.append(descuento_salud_str)
    trabajadores.append(descuento_AFP_str)
    sueldo -= (descuento_AFP + descuento_salud)
    sueldo_str = str(sueldo)
    trabajadores.append(sueldo_str)

def guardar():
    trabajadores_str = '     '.join(trabajadores)
    with open('trabajadores.txt','a') as archivo:
        archivo.write(trabajadores_str + '\n')
    trabajadores.clear()
    
while contador == True:
    m = menu()
    borrar(0.5)
    if m == 1:
        trabajador()
        borrar(0.5)
        cargo()
        borrar(0.5)
        sueldos()
        guardar()
    elif m == 2:
        with open('trabajadores.txt','r') as file:
            for i in file:
                print(i + '\n')
                time.sleep(0.2)
        #solo sirve para volver no sirve para nada este input
        input("presione cualquier enter para volver....")
        borrar(0.5)
    elif m == 3:
        print("saliendo...")
        contador = False
    
        
        
    
