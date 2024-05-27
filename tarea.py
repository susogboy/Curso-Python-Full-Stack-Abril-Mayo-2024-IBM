class Tarea:
    def __init__(self, descripcion):
        # Inicializa la tarea con la descripción proporcionada y establece su estado como no completada
        self.descripcion = descripcion
        self.completada = False

    def marcar_como_completada(self):
        # Cambia el estado de la tarea a completada
        self.completada = True

    def __str__(self):
        # Devuelve una representación en cadena de la tarea, incluyendo su descripción y estado
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"
