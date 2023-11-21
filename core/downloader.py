
import core.methods_downloader as md

class Downloader():
    def __init__(self):
        self.download_video = md._downloadVideo
        self.download_any = md._download_any
        self.download_Playlist = md._downloadPlaylist