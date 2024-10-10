import sys
import os
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from typing import Any
from tkinter.ttk import Label, Frame, Separator, Combobox
from view.components.TreeView import MyTreeview
from view.components.menu_frames import (
    DownloadFrame,
    OutputFrame,
    SavePathFrame,
    StatisticsFrame,
)

# from core.FileDonwloader import FileDownloader

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

    def set_path(self, path):
        self.path = path

    def set_entry1(self, new_entry):
        self.url.set(new_entry)


if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()
