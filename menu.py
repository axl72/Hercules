import sys
import os
import tkinter as tk
from tkinter import ttk
from pathlib import Path
from typing import Any
from tkinter.ttk import Label, Frame, Separator, Combobox
from tkinter.filedialog import askdirectory
from core.downloader import Downloader
from config.config import Config
from threading import Thread
from components.TreeView import MyTreeview
from components.custom_components import Button
from services.Database import DatabaseService



# from core.FileDonwloader import FileDownloader

MY_MUSIC = os.path.join(os.getenv("APPDATA"), "Hercules", "mymusic.json")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("porcentaje de completación: ", percentage_of_completion)


class MainWindow(tk.Tk):
    def __init__(
        self,
        downloader: Downloader,
        config: Config,
        screenName: str | None = None,
        baseName: str | None = None,
        className: str = "Tk",
        useTk: bool = True,
        sync: bool = False,
        use: str | None = None,
        databaseService=DatabaseService(MY_MUSIC),
    ) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.databaseService = databaseService
        self.geometry("500x380")
        self.resizable(False, False)
        self.url = tk.StringVar()

        self.title("Hercules - Download wath you want")
        icon_path = Path("./assets/hercules.ico")
        if not icon_path.exists():
            pass
            # fileDownloader = FileDownloader(
            #    "https://raw.githubusercontent.com/axl72/Hercules/refs/heads/master/assets/hercules.ico",
            #    "./assets",
            # )
            # fileDownloader.download()
        bitmap_path = "./assets/hercules.ico"
        if os.path.exists(bitmap_path):
            self.iconbitmap(bitmap_path)

        self.frame_1 = Frame(self)
        self.frame_2 = Frame(self)
        self.frame_3 = Frame(self)
        self.frame_4 = Frame(self)

        self.boton_1 = tk.Button(
            self.frame_1, text="Download", command=self.download_video
        )
        self.clear_button = tk.Button(
            self.frame_1, text="Clean", command=self.clear_entry1
        )
        self.url_video_label = ttk.Label(self.frame_1, text="Video URL")
        self.config = config
        self.donwloader = downloader
        self.path = tk.StringVar()
        if config.DOWNLOAD_PATH:
            self.path.set(config.DOWNLOAD_PATH)

        self.input_1 = tk.Entry(
            self.frame_1, width=40, font=("Arial 8"), textvariable=self.url
        )

        self.output_extension_label = ttk.Label(self.frame_2, text="Output Extension")
        self.save_in_label = ttk.Label(self.frame_3, text="Save in")
        style = ttk.Style()
        style.configure(
            "TCombobox", padding=[5, 5]
        )  # Ajustar el padding para afectar el alto

        # Crear un Combobox con el estilo personalizado
        self.combo = ttk.Combobox(self.frame_2, width=30, style="TCombobox")
        # self.download_options_combobox = Combobox(self.frame_2, width=40, height=40)
        # self.download_options_combobox["values"] = ("mp3", "mp4")
        self.boton_2 = tk.Button(self.frame_3, text="...", command=self.set_path)
        self.boton_3 = tk.Button(
            self.frame_3, text="Open folder", command=self.see_path
        )
        self.input_2 = tk.Entry(self.frame_3, width=40, textvariable=self.path)

        sep = Separator(self)
        # boton_2 = tk.Button(self, text="Limpiar")

        self.url_video_label.pack(padx=5, pady=2, side="left")
        self.output_extension_label.pack(padx=7, side="left")
        self.save_in_label.pack(padx=5, side="left")
        self.input_1.pack(pady=2, ipadx=2, expand=True, fill="x", side="left", ipady=5)
        self.combo.pack(side="left", expand=True, fill="x")
        self.combo["values"] = (
            "YouTube Video to mp3 (high quality)",
            "Youtube Video to mp4",
        )
        self.combo.current(0)
        # self.download_options_combobox.pack(side="left")
        self.clear_button.pack(padx=5, pady=5, fill="x", side="right")
        self.frame_1.pack(fill=tk.X, side="top", padx=10, pady=2)
        self.input_2.pack(
            pady=5, ipadx=2, expand=True, fill="both", side="left", ipady=5
        )
        self.boton_3.pack(padx=5, pady=5, fill="x", side="right", ipadx=18)
        self.boton_2.pack(padx=5, pady=5, fill="x", side="right", ipadx=18)
        self.frame_2.pack(fill=tk.X, padx=6, side="top")
        self.boton_1.pack(padx=5, pady=5, fill="x", side="right")
        self.frame_3.pack(fill=tk.X, side="top", padx=10)
        sep.pack(side="top", fill="both")

        # Instanciar el treeview
        self.treeview = MyTreeview(self.frame_4)
        self.v_scroll = tk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.treeview.yview
        )
        self.h_scroll = tk.Scrollbar(
            self.frame_4, orient=tk.HORIZONTAL, command=self.treeview.xview
        )
        self.treeview.configure(
            yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set
        )

        # Empaquetar las scrollbars
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.pack(fill="y", padx=10, pady=10)
        if self.databaseService.exist():
            self.treeview.load_data(self.databaseService.read_all())
        self.frame_4.pack(fill=tk.BOTH, side="top")

    def download_video(self):
        self.boton_1.config(state=tk.DISABLED)
        download_thread = Thread(target=self._donwload_thread)
        download_thread.start()

    def _donwload_thread(self):
        url = str(self.input_1.get())
        path = str(self.input_2.get())

        downloaded, data = self.donwloader.download_any(url, path, callback=on_progress)
        if downloaded:
            values = (str(data["size"]) + " Mb", url, path)
            self.databaseService.add_line(
                {
                    "title": data["title"],
                    "size": values[0],
                    "url": url,
                    "saved_path": path,
                }
            )
            self.treeview.add_node("", data["title"], values)
        print(data)
        self.boton_1.config(state=tk.NORMAL)

    def set_path(self):
        path = askdirectory()
        if path:
            path = Path(path)
            self.path.set(path.absolute())

    def see_path(self):
        path = self.path.get()
        os.startfile(path)

    def clear_entry1(self):
        self.url.set("")


if __name__ == "__main__":
    downloader = Downloader()
    config = Config()
    window = MainWindow(downloader, config)
    window.mainloop()
