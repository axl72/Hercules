from pathlib import Path
from core.methods_downloader import (
    _download_any,
    _downloadAudioFromYouTube,
    _downloadPlaylist,
    _downloadVideoFromYouTube,
)
from interfaces.downloader import ServiceDownloader


class Downloader(ServiceDownloader):
    def __init__(self):
        self.download_mp3 = _downloadAudioFromYouTube
        self.download_any = _download_any
        self.download_Playlist = _downloadPlaylist
        self.download_mp4 = _downloadVideoFromYouTube

    def download_audio(self, path: str, url: Path):
        return self.download_any(url, path)

    def download_video(self, path: str, url: Path, res: str):
        return self.download_mp4(url, path, res)
