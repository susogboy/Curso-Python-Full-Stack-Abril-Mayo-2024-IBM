# main.py
from lista_tareas import ListaDeTareas

def mostrar_menu():
    # Imprime el menú de opciones para el usuario
    print("\nMenú de Tareas:")
    print("1. Agregar nueva tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    # Crea una instancia de ListaDeTareas
    lista_de_tareas = ListaDeTareas()

    # Bucle principal del programa para mostrar el menú y ejecutar las opciones seleccionadas
    while True:
        mostrar_menu()  # Muestra el menú de opciones
        try:
            # Solicita al usuario que seleccione una opción y la convierte a entero
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            # Maneja el error si el usuario ingresa un valor no numérico
            print("Error: Por favor, ingrese un número válido.")
            continue

        if opcion == 1:
            # Agregar nueva tarea
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_de_tareas.agregar_tarea(descripcion)
        elif opcion == 2:
            # Marcar tarea como completada
            if lista_de_tareas.mostrar_tareas_pendientes():
                try:
                    posicion = int(input("Ingrese la posición de la tarea a completar: "))
                    lista_de_tareas.marcar_tarea_como_completada(posicion)
                except ValueError:
                    # Maneja el error si el usuario ingresa un valor no numérico
                    print("Error: Por favor, ingrese un número válido.")
        elif opcion == 3:
            # Mostrar todas las tareas
            lista_de_tareas.mostrar_tareas()
        elif opcion == 4:
            # Eliminar tarea
            lista_de_tareas.mostrar_tareas()
            if lista_de_tareas.tareas:
                try:
                    posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                    lista_de_tareas.eliminar_tarea(posicion)
                except ValueError:
                    # Maneja el error si el usuario ingresa un valor no numérico
                    print("Error: Por favor, ingrese un número válido.")
            else:
                print("No hay tareas para eliminar.")
        elif opcion == 5:
            # Salir del programa
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            # Maneja el caso en que el usuario ingrese una opción no válida
            print("Error: Opción no válida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()
