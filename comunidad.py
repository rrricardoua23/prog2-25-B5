from abc import ABC, abstractmethod

class Comunidad(ABC):
    def __init__(self, nombre_comunidad):
        self.nombre_comunidad = nombre_comunidad
        self.presupuesto = 0
    def obtener_info(self):
        return f'Nombre: {self.nombre_comunidad} - Presupuesto: {self.presupuesto}'
    def asignar_presupuesto(self, cantidad):
        self.presupuesto +=cantidad
    @abstractmethod
    def gestionar_centros(self):
        pass
