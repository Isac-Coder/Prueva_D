from gestion_estudiantes import *

while True:
    Menu()
    opcion = input("Escoja una opcion:\n#")

    match opcion:
        case "1":
            Registrar_Estuduantes()
            Limpiar_pantalla()
        case "2":
            Consultar_Estudiante()
            Limpiar_pantalla()
        case "3":
            Buscar_Estudiante()
            Limpiar_pantalla()
        case "4":
            Actualizar_Estudiantes()
            Limpiar_pantalla()
        case "5":
            Eliminar_Estudiante()
            Limpiar_pantalla()
        case "6":
            salir()
        case "7":
            print("\nOpcion invalida")
            input("Presione una tecla para continuar...")
            continue
