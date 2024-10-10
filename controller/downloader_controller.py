from tkinter import Tk


class DownloaderController:
    def __init__(self, view: Tk):
        self.view = view

    def run(self):
        self.view.mainloop()
