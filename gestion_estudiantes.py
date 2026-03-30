import os, csv
from extras import *
Inventario = []

def Menu():
    print("SELECCIONE UNA OPCION")
    print("1. Registrar Estudiante\n2. Consultar Estudiante\n3. Buscar Estudiante\n4. Actualizar Estudiante\n5. Eliminar Estudiant\n6. Salir")

def Registrar_Estuduantes():
    while True:
        Limpiar_pantalla()
        try:
            ID = input("Ingrese su ID:\n# ")
            if not ID.isdigit():
                raise ValueError
            else:
                ID = int(ID)
                if ID <= 0:
                    raise ValueError
                ID = int(ID)
        except ValueError:
            print(f"El ID {ID} ingresado no es valido")
            input("Presione Enter para continuar...")
            continue

        try:
            NOMBRE = input("Ingrese el nombre del estudiante\n# ")
            if not NOMBRE.strip() or not all(c.isalpha() or c.isspace() for c in NOMBRE):
                print(f"El Nombre {NOMBRE} ingresado no es valido")
                input("Presione Enter para continuar...")
                continue
            else:
                NOMBRE = NOMBRE.strip().title()

        except ValueError:
            print("Por favor ingrese un nombre valido")

        try:
            EDAD = input("Ingrese su edad:\n# ")
            if not EDAD.isdigit():
                raise ValueError
            else:
                EDAD = int(EDAD)
                if EDAD <= 0:
                    raise ValueError
                EDAD = int(EDAD)
        except ValueError:
            print(f"El ID {EDAD} ingresado no es valido")
            input("Presione Enter para continuar...")
            continue

        try:
            CURSO = input("Ingrese el nombre del curso o programa:\n# ")
            if not CURSO.strip() or not all(c.isalpha() or c.isspace() for c in CURSO):
                raise ValueError
            else:
                CURSO = CURSO.strip().title()
        except ValueError:
            print(f"El CURSO {CURSO} ingresado no es valido")
            input("Presione Enter para continuar...")
            continue
        
        try:
            ESTADO = input("Ingrese el estado en el que se encuentra (1. Activo  / 2. Inactivo):\n#")
            if ESTADO not in ["1", "2", "Activo", "Inactivo"]:
                raise ValueError
            else:
                
                if ESTADO == "1" or ESTADO == "Activo":
                    ESTADO = "Activo"
                    continuar = "no"
                elif ESTADO == "2" or ESTADO == "Inactivo":
                    ESTADO = "Inactivo"
                    continuar = "no"
                else:
                    raise ValueError
                ESTADO = str(ESTADO)
        except ValueError:
            print(f"El ESTADO {ESTADO} ingresado no es valido")
            input("Presione Enter para continuar...")
            continue
        if any(c["ID"] == ID for c in Inventario):
            print(f"El ID {ID} ya está registrado")
            input("Presione Enter para continuar...")
            continue
        Usuario = {
            "ID":ID,
            "Nombre":NOMBRE,
            "Edad":EDAD,
            "CURSO":CURSO,
            "ESTADO":ESTADO
        }
        
        Inventario.append(Usuario)

        print(f"Estidiante {NOMBRE} registrado exitosamente")
        opcion = input("¿Desea ingresar otro estudiante? (si/no): ").lower()
        if opcion == "no":
            break

def Consultar_Estudiante():
    if not Inventario:
        print("No hay Estudiantes en la base de datos")
        input("Presione ENTER para continuar...")
        return
    else:
        try:
            ID = input("Ingrese el ID del cliente a consultar:\n# ")
            if not ID.isdigit():
                raise ValueError
            ID = int(ID)
            if ID <= 0:
                raise ValueError
        except ValueError:
            print("El ID ingresado no es valido")
            input("Presione Enter para continuar...")
            return
    
    for Usuario in Inventario:
        if Usuario["ID"] == ID:
            print(f"ID: {Usuario['ID']}")
            print(f"Nombre: {Usuario['Nombre']}")
            print(f"Edad: {Usuario['Edad']}")
            print(f"CURSO: {Usuario['CURSO']}")
            print(f"Estado: {Usuario['ESTADO']}")
            break
    else:
        print(f"No se encontró un cliente con el ID {ID}")
        input("Presione Enter para continuar...")


def Buscar_Estudiante():
    if not Inventario:
        print("No hay Estudiante es la base de datos")
        input("Presione Enter para continuar...")
        return
    busqueda = input("Ingrese el ID o el Nombre del estudiante a consultar:\n# ").strip().title()

    encontrado = False

    for usuario in Inventario:
        if str(usuario["ID"]) == busqueda or usuario["Nombre"] == busqueda:
            print("-" * 20)
            print(f"ID: {usuario['ID']}")
            print(f"Nombre: {usuario['Nombre']}")
            print(f"Edad: {usuario['Edad']}")
            print(f"CURSO: {usuario['CURSO']}")
            print(f"ESTADO: {usuario['ESTADO']}")
            encontrado = True
            break

    if not encontrado:
        print(f"No se encontró ningún estudiante que coincida con: {busqueda}")
    
    input("Presione Enter para continuar...")
        
def Actualizar_Estudiantes():
    if not Inventario:
        print("No hay Estudiantes en la base de datos")
        input("Presione Enter para continuar...")
        return
    try:
        ID = input("Ingrese el ID del cliente a actualizar:\n# ")
        ID = int(ID)
        if ID <= 0:
            raise ValueError
    except ValueError:
        print("El ID ingresado no es válido")
        input("Presione Enter para continuar...")
        return
    
    estudiante_encontrado = None
    for Usuario in Inventario:
        if Usuario["ID"] == ID:
            estudiante_encontrado = Usuario
            break

    if not estudiante_encontrado:
        print(f"No se encontró un cliente con el ID {ID}")
        input("Presione Enter para continuar...")
        return

    print("Datos actuales del estudiante:")
    print(f"ID: {estudiante_encontrado['ID']}")
    print(f"Nombre: {estudiante_encontrado['Nombre']}")
    print(f"Edad: {estudiante_encontrado['Edad']}")
    print(f"CURSO: {estudiante_encontrado['CURSO']}")
    print(f"ESTADO: {estudiante_encontrado['ESTADO']}")
    print("\nIngrese los nuevos datos:")

    while True:
        try:
            print("Digite el nuvo nombre del curso deje vacío para mantener:")
            nuevo_curso = input("# ")
            if nuevo_curso.strip():
                estudiante_encontrado["CURSO"] = nuevo_curso
            else:
                raise ValueError
            break
        except ValueError:
            print("Estado inválido")

    print("Cliente actualizado exitosamente")
    input("Presione Enter para continuar...")

    while True:
        try:
            print("Elija un nuevo estado (1. Activo, 2. Inactivo, deje vacío para mantener):")
            nuevo_estado = input("# ")
            if nuevo_estado.strip():
                if nuevo_estado in ["1", "Activo"]:
                    estudiante_encontrado["ESTADO"] = "Activo"
                elif nuevo_estado in ["2", "Inactivo"]:
                    estudiante_encontrado["ESTADO"] = "Inactivo"
                else:
                    raise ValueError
            break
        except ValueError:
            print("Estado inválido")
    print("Cliente actualizado exitosamente")
    input("Presione Enter para continuar...")

def Eliminar_Estudiante():

    if not Inventario:
        print("No hay Estudiantes en base de datos")
        input("Presione Enter para continuar...")
        return
    try:
        ID = input("Ingrese el ID del estudiante a eliminar:\n# ")
        ID = int(ID)
        if ID <= 0:
            raise ValueError
    except ValueError:
        print("El ID ingresado no es válido")
        input("Presione Enter para continuar...")
        return
    
    for Usuario in Inventario:
        if Usuario["ID"] == ID:
            Inventario.remove(Usuario)
            print(f"Estudiante con ID {ID} eliminado exitosamente")
            input("Presione Enter para continuar...")
            return
    print(f"No se encontró un cliente con el ID {ID}")
    input("Presione Enter para continuar...")

def salir():
    exit()