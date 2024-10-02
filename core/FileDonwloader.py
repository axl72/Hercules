import requests
import os
from pathlib import Path


# class FileDownloader:
#     def __init__(self, url: str, relative_path: Path):
#         self.url = url
#         self.relative_path = relative_path

#     def download(self):
#         # Crear directorios si no existen
#         folder = Path(self.relative_path)
#         if not folder.exists():
#             os.makedirs(folder)

#         # Realizar la solicitud GET
#         response = requests.get(self.url)

#         # Verificar si la solicitud fue exitosa
#         if response.status_code == 200:
#             # Guardar el archivo en la ruta especificada
#             with open(self.relative_path + "/hercules.ico", "wb") as file:
#                 file.write(response.content)
#             print(f"Archivo descargado con éxito en: {self.relative_path}")
#         else:
#             print(f"Error al descargar el archivo: {response.status_code}")
