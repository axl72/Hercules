from abc import ABC, abstractmethod


# TODO: definir los métodos necesarios para que cualquier interfaz pueda funcionar con el controlador. Esto es más una cuestión de lógica que de programación.
class MainMenu(ABC):
    @abstractmethod
    def create_menu(self):
        """Método para crear un menú."""
        pass
