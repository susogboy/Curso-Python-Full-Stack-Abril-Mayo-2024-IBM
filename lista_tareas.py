from tarea import Tarea

class ListaDeTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)

    def marcar_tarea_como_completada(self, posicion):
        try:
            self.tareas[posicion].marcar_como_completada()
        except IndexError:
            print("Error: Posición de tarea no válida.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            for indice, tarea in enumerate(self.tareas):
                print(f"{indice}. {tarea}")

    def eliminar_tarea(self, posicion):
        try:
            del self.tareas[posicion]
        except IndexError:
            print("Error: Posición de tarea no válida.")
