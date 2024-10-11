from enum import Enum


class OutputFormat(Enum):
    MP3_ALTA = ("YouTube Video to mp3 (high quality)", "mp3", None)
    MP4_144P = ("YouTube Video to mp4 144p (Poor Definition)", "mp4-144p", "144p")
    MP4_240P = ("YouTube Video to mp4 240p (Low Definition)", "mp4-240p", "240p")
    MP4_360P = ("YouTube Video to mp4 360p (Basic Definition)", "mp4-360p", "360p")
    MP4_480P = ("YouTube Video to mp4 480p (Medium Definition)", "mp4-480p", "480p")
    MP4_720P = ("YouTube Video to mp4 720p (High Definition)", "mp4-720p", "720p")
    MP4_1080P = ("YouTube Video to mp4 1080p60 (Full HD)", "mp4-1080p", "1080p")

    def __init__(self, display_text, output_value, resolution):
        self.display_text = display_text  # Texto para el combobox
        self.output_value = output_value  # Valor usado en el controlador
        self.resolution = resolution  # Resolución si es video

    def __str__(self):
        return self.output_value
