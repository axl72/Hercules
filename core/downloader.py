from pathlib import Path
from core.methods_downloader import (
    _download_any,
    _downloadAudioFromVideo,
    _downloadPlaylist,
)
from interfaces.downloader import ServiceDownloader


class Downloader(ServiceDownloader):
    def __init__(self):
        self.download_video = _downloadAudioFromVideo
        self.download_any = _download_any
        self.download_Playlist = _downloadPlaylist

    def download(self, path: str, url: Path):
        return self.download_video(url, path)
