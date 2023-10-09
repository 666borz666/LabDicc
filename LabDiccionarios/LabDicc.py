#Elaborado por: Ignacio Garcia y Daniel Campos
#Fecha de Creación: 02/10/2023 9:00am
#Última modificación: 02/10/2023 10:35am
#Versión:3.11.3
#Variable global
diccDent={}
#Importacion
import pickle
#Definicion de funciones
def graba(nomArchGrabar,lista):
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
    except:
        print("Error al grabar el archivo.", nomArchGrabar)
    return

def lee (nomArchLeer):
    dicc={}
    try:
        f=open(nomArchLeer,"rb")
        dicc = pickle.load(f)
        f.close()
    except:
        print("Error al leer el archivo.", nomArchLeer)
    return dicc

def agregarPaciente(diccDent):
    try:
        ced = input("Ingrese su Cédula: ")
        nom = input("Ingrese el Nombre: ")
        apellido1 = input("Ingrese su Primer apellido: ")
        apellido2 = input("Ingrese su Segundo apellido: ")
        obs = (input("Observación: "))
        datos = [(nom, apellido1, apellido2), (obs)]
    except ValueError:
        print("Ingrese un valor válido")
        return
    diccDent[ced] = datos
    graba("clinica.txt",diccDent)
    print("Los datos se han registrado con éxito")

def actualizarPaciente(diccDent,ced):
    print("Cédula:",ced)
    try:
        observacion = input("Ingrese la nueva observación: ")
        confirmacion = int((input("¿Está seguro de actualizar la observación? (1-Si, 2-No): ")))
    except ValueError:  
        print("Ingrese un valor válido")
        return
    if confirmacion == 1  or confirmacion == 2:
        if confirmacion == 1:
            diccDent[ced][1] = observacion
            print("La observación se ha actualizado con éxito")
            graba("clinica.txt",diccDent)
        elif confirmacion == 2:
            print("La observación no se ha actualizado")

def eliminarPaciente(diccDent,ced):
    try:
        del(diccDent[ced])
        print("El paciente ha sido eliminado satisfactoriamente. ")
        graba("clinica.txt",diccDent)
        return diccDent
    except KeyError:
        print("El paciente no existe")
        return diccDent

def mostrarPaciente(diccDent,ced):
    try:
        infoPaciente = diccDent[ced]
        print("Cédula:",ced)
        print("Datos del paciente:")
        print("Nombre:",(infoPaciente[0][0]))
        print("Primer apellido:",(infoPaciente[0][1]))
        print("Segundo apellido:",(infoPaciente[0][2]))
        print ("Observación:",infoPaciente[1])
        print ("-------------------")
    except KeyError:
        print("El paciente no existe.")
    return

def menu():
    diccDent=lee("clinica")
    while True:
        try:
            print("*************************************************")
            print("Bienvenido al sistema de la clínica dental")
            print("1-Insertar paciente.")
            print("2-Actualizar paciente.")
            print("3-Eliminar paciente.")
            print("4-Mostrar paciente.")
            print("5-Salir")
            print("*************************************************")
            opcion = int(input("Opción: "))
            print()
            if opcion == 1:
                agregarPaciente(diccDent)
            elif opcion == 2:
                ced = input("Indique el numero de cedula: ")
                actualizarPaciente(diccDent,ced)
            elif opcion == 3:
                ced = input("Indique el numero de cedula: ")
                eliminarPaciente(diccDent,ced)
            elif opcion == 4:
                ced = input("Indique la cedula a mostrar: ")
                mostrarPaciente(diccDent,ced)
            elif opcion == 5:
                graba("clinica.txt",diccDent)
                break
        except ValueError:
            print("Ingrese un valor válido")
    return
#Programa Principal
menu()