class Medicamento:
    def __init__(self, nombre, dosis, tipo, precio, fecha_caducidad, alergenos = None):
        self.nombre = nombre
        self.dosis = dosis
        self.tipo = tipo
        self.precio = precio
        self.fecha_caducidad = fecha_caducidad
        if alergenos is not None:
            self.alergenos = alergenos
    def obtener_info(self):
        info = (f'Medicamento: {self.nombre}\n'
                f'Tipo: {self.tipo}\n'
                f'Precio: {self.precio}\n'
                f'Fecha: {self.fecha_caducidad}\n'
                f'Alergenos: {self.alergenos}\n')