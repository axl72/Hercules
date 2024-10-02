import tkinter as tk


class Button(tk.Button):
    botones_instanciados = 0

    def __init__(self, frame, command=None, text: str = ""):
        Button.botones_instanciados += 1
        super().__init__(frame, text=f"Boton de ejemplo {Button.botones_instanciados}")
        self.configure(
            command=self.destroy,
            width=20,
            height=1,
            padx=5,
            pady=5,
            relief="solid",
            bg="#F57A81",
        )
