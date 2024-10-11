from abc import ABC, abstractmethod
from pathlib import Path


# TODO: definir los métodos necesarios para que cualquier interfaz pueda funcionar con el controlador. Esto es más una cuestión de lógica que de programación.
class MainMenu(ABC):
    @abstractmethod
    def get_video_url() -> str:
        pass

    @abstractmethod
    def set_video_url(url: str) -> None:
        pass

    @abstractmethod
    def set_command_download_button(download_function: callable) -> None:
        pass

    @abstractmethod
    def set_command_clear_button(clear_function: callable) -> None:
        pass

    @abstractmethod
    def get_outputextension() -> str:
        pass

    @abstractmethod
    def get_pathsave_input() -> str:
        pass

    @abstractmethod
    def set_pathsave_input(new_pathsave: Path) -> None:
        pass

    @abstractmethod
    def set_command_pathsave_button(pathsave_function: callable) -> None:
        pass

    @abstractmethod
    def set_command_openfolder_button(openfolder_function: callable) -> None:
        pass

    @abstractmethod
    def set_trewview() -> None:
        pass

    @abstractmethod
    def raise_error_dialog() -> None:
        pass

    @abstractmethod
    def add_register_trewview() -> None:
        pass
