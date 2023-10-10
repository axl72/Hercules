import tkinter as tk
from typing import Any
from tkinter.ttk import Button, Label, Frame

class Button(tk.Button):
    botones_instanciados = 0
    def __init__(self, command=None,text:str=""):
        Button.botones_instanciados +=1
        super().__init__(text=f"Boton de ejemplo {Button.botones_instanciados}")
        self.configure(command=self.destroy, width=20, height=2, padx=5, pady=5, relief="solid", bg="#F57A81")
    
    
        
class Entry(tk.Entry):
    def __init__(self):
        super().__init__()
        

class MainWindow(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.geometry("400x400")
        self.frame_1 = Frame()
        self.boton_1 = Button()
        self.boton_1.pack(self.frame_1,padx=5, pady=5, fill="x", side="left")
        self.input_1 = Entry()
        self.input_1.pack(self.frame_1,padx=5, pady=5, fill="x", side="left")
        # self.label = Label(text="Texto de prueba")
        self.frame_1.pack(side="top")
        # self.label.pack(side="top")
    
if __name__ == "__main__":
    window = MainWindow()
    window.mainloop()