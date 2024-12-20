from interfaces.menu import MainMenu
from interfaces.downloader import ServiceDownloader
from core.config import Config
from tkinter.filedialog import askdirectory
from pathlib import Path
from threading import Thread
from services.Database import DatabaseService
import os
from util.datatypes import OutputFormat


class DownloaderController:
    def __init__(
        self, view: MainMenu, downloader: ServiceDownloader, database: DatabaseService
    ):
        self.view = view
        self.database = database
        self.downloader = downloader
        self.view.set_command_clear_button(self._clear)
        self.view.set_pathsave_input(Config.DOWNLOAD_PATH)
        self.view.set_command_pathsave_button(self._set_folder)
        self.view.set_command_openfolder_button(self._open_download_directory)
        self.view.set_command_download_button(self._download_thread)

        if self.database.exist():
            self.view.set_trewview(self.database.read_all())

    def _clear(self):
        self.view.set_video_url("")

    def _set_folder(self):
        path = askdirectory()
        if path:
            path = Path(path)
            self.view.set_pathsave_input(path)

    def _open_download_directory(self):
        path = self.view.get_pathsave_input()
        os.startfile(path)

    def _download(self):
        downloaded = False
        url = self.view.get_video_url()
        path = self.view.get_pathsave_input()
        output = self.view.get_outputextension()
        print(f"Downloading {url} to {path} with format {output}")
        match output:
            case OutputFormat.MP4_720P.output_value:
                downloaded, data = self.downloader.download_video(path, url, "720p")
            case OutputFormat.MP3_ALTA.output_value:
                downloaded, data = self.downloader.download_audio(path, url)
            case OutputFormat.MP4_1080P.output_value:
                downloaded, data = self.downloader.download_video(path, url, "1080p")
            case OutputFormat.MP4_144P.output_value:
                downloaded, data = self.downloader.download_video(path, url, "144p")
            case OutputFormat.MP4_240P.output_value:
                downloaded, data = self.downloader.download_video(path, url, "240p")
            case OutputFormat.MP4_360P.output_value:
                downloaded, data = self.downloader.download_video(path, url, "360p")
            case _:
                print("Format not supported")
                raise Exception("Format not supported")

        if downloaded:
            print("Archivo descargado, registrando información")
            values = (str(data["size"]) + " Mb", url, path)
            self.database.add_line(
                {
                    "title": data["title"],
                    "size": values[0],
                    "url": url,
                    "saved_path": path,
                }
            )
            self.view.add_register_trewview(data["title"], values)
            print(data)
        print("download completed")

    def _download_thread(self):
        print("Downloading")
        self.view.set_disabled_download_button()
        thread = Thread(target=self._download)
        thread.start()
        self.view.set_enable_download_button()

    def run(self):
        self.view.mainloop()
