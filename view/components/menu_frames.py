from tkinter import ttk
import tkinter as tk
from view.components.TreeView import MyTreeview


class DownloadFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        # Instancia de componentes
        self.urlVar = tk.StringVar()  # StringVar para la URL
        self.download_button = tk.Button(self, text="Download")
        self.clear_button = tk.Button(self, text="Clear")  # Instancia de Clear Button
        self.video_url_label = ttk.Label(
            self, text="Video URL"
        )  # Instancia de URL Label

        self.video_url_input = tk.Entry(
            self, width=40, font=("Arial 8"), textvariable=self.urlVar
        )

        # Packs de componentes

        self.download_button.pack(padx=5, pady=5, fill="x", side="right")
        self.video_url_label.pack(padx=5, pady=2, side="left")
        self.video_url_input.pack(
            pady=2, ipadx=2, expand=True, fill="x", side="left", ipady=5
        )
        self.clear_button.pack(padx=5, pady=5, fill="x", side="right")


class OutputFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.combo = ttk.Combobox(self, width=30, style="TCombobox")
        self.combo.config(state="readonly")
        self.combo["values"] = (
            "YouTube Video to mp3 (high quality)",
            "Youtube Video to mp4",
        )
        self.output_extension_label = ttk.Label(self, text="Output Extension")
        self.combo.current(0)

        self.output_extension_label.pack(padx=7, side="left")
        self.combo.pack(side="left", expand=True, fill="x")


class SavePathFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):

        self.savepath = tk.StringVar()  # StringVar para el save path
        self.save_in_label = ttk.Label(self, text="Save in")

        self.select_path_button = tk.Button(self, text="...")
        self.open_savepath_directory_button = tk.Button(self, text="Open folder")
        self.savepath_input = tk.Entry(self, width=40, textvariable=self.savepath)

        # Packs

        self.save_in_label.pack(padx=5, side="left")
        self.select_path_button.pack(padx=5, pady=5, fill="x", side="right", ipadx=18)
        self.open_savepath_directory_button.pack(
            padx=5, pady=5, fill="x", side="right", ipadx=18
        )

        self.savepath_input.pack(
            pady=5, ipadx=2, expand=True, fill="both", side="left", ipady=5
        )


class StatisticsFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()

    def create_widgets(self):
        self.treeview = MyTreeview(self)  # Instanciar el treeview
        self.h_scroll = tk.Scrollbar(
            self, orient=tk.HORIZONTAL, command=self.treeview.xview
        )
        self.v_scroll = tk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.treeview.yview
        )
        self.treeview.configure(
            yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set
        )
        self.treeview.pack(fill="y", padx=10, pady=10)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.treeview.pack(fill="y", padx=10, pady=10)
