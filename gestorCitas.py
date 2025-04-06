from typing import List
from abc import ABC, abstractmethod

class CitaBase(ABC):
    """
    Clase abstracta que define la estructura báscia de una cita.

    -Métodos:
    ----------
        - obtener_informacion: Devuelve la información de la cita en forma str.
          Recibe self como único parámetro
    """

    @abstractmethod
    def obtener_informacion(self) -> str:
        """
        Método abstracto que debe implementarse para retornar la información de la cita.
        """
        pass

class Cita(CitaBase):
    """
    Clase que representa una cita en el centro de salud.

    Atributos:
    ----------
        id_cita (int) : Identificador único de la cita
        paciente (str) : Nombre del paciente
        fecha (str) : Fecha y hora de la cita (formato : AAAA-MM-DD HH:MM)
        tipo (str): Tipo de cita (Telefónica, Presencial, Urgencia, Consulta, etc.)
        """
