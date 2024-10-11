from interfaces.menu import MainMenu
from interfaces.downloader import ServiceDownloader
from core.config import Config
from tkinter.filedialog import askdirectory
from pathlib import Path
from threading import Thread
from services.Database import DatabaseService
import os


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
        url = self.view.get_video_url()
        path = self.view.get_pathsave_input()
        output = self.view.get_outputextension()

        match output:
            case "mp4":
                self.view.raise_error_dialog(
                    "Error", "This format is not supported yet"
                )
                return

            case "mp3":

                downloaded, data = self.downloader.download(path, url)
                if downloaded:
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
                self.view.set_enable_download_button()
                return

    def _download_thread(self):
        print("Downloading")
        self.view.set_disabled_download_button()
        thread = Thread(target=self._download)
        thread.start()

    def run(self):
        self.view.mainloop()
