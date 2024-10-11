import sys
import os
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter.ttk import Label, Separator
from view.components.TreeView import MyTreeview
from view.components.menu_frames import (
    DownloadFrame,
    OutputFrame,
    SavePathFrame,
    StatisticsFrame,
)
from interfaces.menu import MainMenu

MY_MUSIC = os.path.join(os.getenv("APPDATA"), "Hercules", "mymusic.json")


class MainWindow(tk.Tk, MainMenu):
    def __init__(
        self,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.__make_config()

        self.download_frame = DownloadFrame(self)
        self.output_frame = OutputFrame(self)
        self.savepath_frame = SavePathFrame(self)
        self.statisctis_frame = StatisticsFrame(self)

        style = ttk.Style()
        style.configure(
            "TCombobox", padding=[5, 5]
        )  # Ajustar el padding para afectar el alto
        sep = Separator(self)

        self.download_frame.pack(fill=tk.X, side="top", padx=10, pady=2)
        self.output_frame.pack(fill=tk.X, padx=6, side="top")
        self.savepath_frame.pack(fill=tk.X, side="top", padx=10)
        sep.pack(side="top", fill="both")
        self.statisctis_frame.pack(fill=tk.BOTH, side="top")

    def __make_config(self):
        self.geometry("500x380")  # Tamaño de la ventana
        self.resizable(False, False)  # Valor de redimensión
        self.title("Hercules - Download wath you want")  # Título de la ventana
        self.bitmap_path = Path("./assets/hercules.ico")  # Path del ícono de la ventana
        if self.bitmap_path.exists():
            self.iconbitmap(self.bitmap_path)  # Asignación del ícono de la ventana

    def set_command_download_button(self, download_function: callable) -> None:
        self.download_frame.download_button.config(command=download_function)

    def set_command_clear_button(self, clear_function: callable) -> None:
        self.download_frame.clear_button.config(command=clear_function)

    def get_video_url(self) -> None:
        return self.download_frame.urlVar.get()

    def set_video_url(self, url) -> None:
        return self.download_frame.urlVar.set(url)

    def get_outputextension(self) -> str:
        output = self.output_frame.combo.get()
        if output == "YouTube Video to mp3 (high quality)":
            return "mp3"
        elif output == "Youtube Video to mp4 720p (High Definition)":
            return "mp4-720p"
        elif output == "YouTube Video to mp4 1080p60 (Full HD)":
            return "mp4-1080p"
        else:
            return None  # En caso de que no haya una opción válida seleccionada

    def get_pathsave_input(self) -> str:
        return self.savepath_frame.savepath.get()

    def set_pathsave_input(self, new_pathsave: Path) -> None:
        self.savepath_frame.savepath.set(new_pathsave)

    def set_command_openfolder_button(self, openfolder_function: callable) -> None:
        self.savepath_frame.open_savepath_directory_button.config(
            command=openfolder_function
        )

    def add_register_trewview(
        self, title: str, music_metadata: tuple[str, str, str]
    ) -> None:
        self.statisctis_frame.treeview.add_node("", title, music_metadata)

    def set_trewview(self, registers: list[dict]) -> None:
        self.statisctis_frame.treeview.load_data(registers)

    def set_enable_download_button(self) -> None:
        self.download_frame.download_button.config(state=tk.NORMAL)

    def set_disabled_download_button(self) -> None:
        self.download_frame.download_button.config(state=tk.DISABLED)

    def set_command_pathsave_button(self, pathsave_function: callable) -> None:
        self.savepath_frame.select_path_button.config(command=pathsave_function)

    def raise_error_dialog(self, title, error) -> None:
        tk.messagebox.showerror(
            title=title,
            message=error,
        )


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
