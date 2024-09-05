from tkinter.ttk import Treeview


class MyTreeview(Treeview):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        # Puedes configurar opciones adicionales aquí
        self.configure(columns=("1", "2", "3"))
        self.heading("#0", text="Title")
        self.heading("1", text="Size")
        self.heading("2", text="URL")
        self.heading("3", text="Saved in")

        self.column("#0", width=295)
        self.column("1", width=95, anchor="center")
        self.column("2", width=300)
        self.column("3", width=300)
        # Configurar otras características o atributos personalizados
        self.bind("<Button-1>", self.on_click)

    def add_node(self, parent, text, values=()):
        """Método para agregar un nodo al árbol."""
        self.after(0, self._insert_node, parent, text, values)

    def _insert_node(self, parent, text, values):
        self.insert(parent, "end", text=text, values=values)

    def on_click(self, event):
        """Método para manejar eventos de clic en el Treeview."""
        item = self.identify_row(event.y)
        if item:
            print(f"Clic en el ítem: {self.item(item, 'text')}")

    def load_data(self, registers):
        for register in registers:
            self.add_node(
                "",
                register["title"],
                (register["size"], register["url"], register["saved_path"]),
            )
