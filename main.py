from lista_tareas import ListaDeTareas

def mostrar_menu():
    print("\nMenú de Tareas:")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    lista_de_tareas = ListaDeTareas()

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == 2:
            try:
                posicion = int(input("Ingrese la posición de la tarea a completar: "))
                lista_de_tareas.marcar_tarea_como_completada(posicion)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == 3:
            lista_de_tareas.mostrar_tareas()
        elif opcion == 4:
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                lista_de_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
        elif opcion == 5:
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
