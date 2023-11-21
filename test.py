import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QFrame, QVBoxLayout, QLineEdit, QPushButton, QFileDialog
from pathlib import Path
from controller.downloader import download_any


class CustomButton(QPushButton):
    botones_instanciados = 0

    def __init__(self, frame, text: str = ""):
        CustomButton.botones_instanciados += 1
        super().__init__(f"Boton de ejemplo {CustomButton.botones_instanciados}", frame)
        self.clicked.connect(self.close)
        self.setMinimumWidth(20)
        self.setMinimumHeight(1)
        self.setFixedWidth(150)
        self.setStyleSheet("background-color: #F57A81;")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 400)
        self.url = ""
        self.path = ""

        self.frame_1 = QFrame(self)
        self.boton_1 = QPushButton("Descargar", self.frame_1, clicked=self.download)
        self.clear_button = QPushButton("Borrar", self.frame_1, clicked=self.clear_entry1)
        self.input_1 = QLineEdit(self.frame_1)
        self.input_1.setFixedWidth(300)

        self.frame_2 = QFrame(self)
        self.boton_2 = QPushButton("...", self.frame_2, clicked=self.set_path)
        self.input_2 = QLineEdit(self.frame_2)
        self.input_2.setFixedWidth(300)

        label = QLabel("Texto de prueba", self)

        layout = QVBoxLayout()
        layout.addWidget(self.input_1)
        layout.addWidget(self.boton_1)
        layout.addWidget(self.clear_button)
        self.frame_1.setLayout(layout)

        layout = QVBoxLayout()
        layout.addWidget(self.input_2)
        layout.addWidget(self.boton_2)
        self.frame_2.setLayout(layout)

        self.setCentralWidget(self.frame_1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.setCentralWidget(self.frame_1)
        self.setCentralWidget(self.frame_2)

        self.show()

    def download(self):
        self.url = self.input_1.text()
        self.path = self.input_2.text()

        print(f"Url selected is '{self.url}'")
        print(f"Path selected is '{self.path}'")
        download_any(self.url, self.path)

    def set_path(self):
        path = QFileDialog.getExistingDirectory(self, "Seleccionar carpeta", str(Path.home()))
        path = Path(path)
        self.input_2.setText(str(path.absolute()))

    def clear_entry1(self):
        self.input_1.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
