import sys
import tkinter as tk
from pathlib import Path
from typing import Any
from tkinter.ttk import Button, Label, Frame, Separator
from tkinter.filedialog import askdirectory
from core.downloader import Downloader
from core.config import Config
from threading import Thread


class Button(tk.Button):
    botones_instanciados = 0
    def __init__(self, frame,command=None,text:str=""):
        Button.botones_instanciados +=1
        super().__init__(frame, text=f"Boton de ejemplo {Button.botones_instanciados}")
        self.configure(command=self.destroy, width=20, height=1, padx=5, pady=5, relief="solid", bg="#F57A81")

class MainWindow(tk.Tk):
    def __init__(self, downloader:Downloader, config:Config,screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("400x400")
        self.url = tk.StringVar()
        self.frame_1 = Frame(self)
        self.boton_1 = tk.Button(self.frame_1, text="Descargar", command=self.download_video)
        self.clear_button = tk.Button(self.frame_1, text="Borrar", command=self.clear_entry1)
        self.config = config
        self.donwloader = downloader
        self.path = tk.StringVar()
        if config.DOWNLOAD_PATH:
            self.path.set(config.DOWNLOAD_PATH)
 
        self.input_1 = tk.Entry(self.frame_1, width=40, textvariable=self.url)

        self.frame_2 = Frame(self)
        self.boton_2 = tk.Button(self.frame_2, text="...", command=self.set_path)
        self.input_2 = tk.Entry(self.frame_2, width=40, textvariable=self.path)

        sep = Separator(self)
        # boton_2 = tk.Button(self, text="Limpiar")

        self.input_1.pack(padx=5, pady=5, fill="x", side="left", ipady=5)
        self.boton_1.pack(padx=5, pady=5, fill="x", side="right")
        self.clear_button.pack(padx=5, pady=5, fill="x", side="right")
        self.frame_1.pack(side="top")
        self.input_2.pack(padx=5, pady=5, fill="x", side="left", ipady=5)
        self.boton_2.pack(padx=5, pady=5, fill="x", side="right", ipadx=18)
        self.frame_2.pack(side="top")
        sep.pack(side="top", fill="both")


        label = Label(self,text="Texto de prueba")
        label.pack(side="top")
        # self.label.pack(side="top")
    
    def download_video(self):
        self.boton_1.config(state=tk.DISABLED)
        download_thread = Thread(target=self._donwload_thread)
        download_thread.start()
    
    def _donwload_thread(self):
        url = str(self.input_1.get())
        path = str(self.input_2.get())
        
        print(f"Url selected is '{url}'")
        print(f"Path selected is '{path}'")

        self.donwloader.download_any(url, path)
        self.boton_1.config(state=tk.NORMAL)
    
    def set_path(self):
        path = askdirectory()
        path = Path(path)
        self.path.set(path.absolute())
    
    def clear_entry1(self):
        self.url.set("")


    
if __name__ == "__main__":
    downloader = Downloader()
    config = Config()
    window = MainWindow(downloader, config)
    window.mainloop()