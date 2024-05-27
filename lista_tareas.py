from tarea import Tarea

class ListaDeTareas:
    def __init__(self):
        # Inicializa una lista vacía para almacenar las tareas
        self.tareas = []

    def agregar_tarea(self, descripcion):
        # Crea una nueva tarea con la descripción proporcionada y la añade a la lista de tareas
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_tarea_como_completada(self, posicion):
        # Marca una tarea específica como completada, basada en su posición en la lista
        try:
            self.tareas[posicion].marcar_como_completada()
        except IndexError:
            # Maneja el error si la posición proporcionada no es válida
            print("Error: Posición de tarea no válida.")

    def mostrar_tareas(self):
        # Muestra todas las tareas en la lista junto con su índice
        if not self.tareas:
            # Si no hay tareas en la lista, muestra un mensaje indicando que no hay tareas pendientes
            print("No hay tareas pendientes.")
        else:
            for indice, tarea in enumerate(self.tareas):
                # Muestra el índice y la descripción de cada tarea
                print(f"{indice}. {tarea}")

    def eliminar_tarea(self, posicion):
        # Elimina una tarea específica de la lista, basada en su posición
        try:
            del self.tareas[posicion]
        except IndexError:
            # Maneja el error si la posición proporcionada no es válida
            print("Error: Posición de tarea no válida.")
