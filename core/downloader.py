from pathlib import Path
import core.methods_downloader as md
import core.service_downloader as sd


class Downloader(sd.ServiceDownloader):
    def __init__(self):
        self.download_video = md._downloadAudioFromVideo
        self.download_any = md._download_any
        self.download_Playlist = md._downloadPlaylist

    def download(self, path: str, url: Path):
        return self.download_video(url, path)
