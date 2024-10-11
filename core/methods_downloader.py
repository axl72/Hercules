from pytube import Playlist, YouTube
import logging
from colorama import Fore, Back, Style, init
from pathlib import Path

init()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def _downloadVideoFromYouTube(
    url: str, path: Path, res: str, prefix: str = ""
) -> tuple[bool, dict]:
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.default_filename
        size_mb = round(stream.filesize / (1024 * 1024), 2)
        stream.download(output_path=path, filename=filename, filename_prefix=prefix)
        return (True, {"title": yt.title, "size": size_mb})

    except Exception as e:
        print(e)
        return (False, yt.title)


def _downloadAudioFromYouTube(url, path, prefix=""):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        file_name = stream.default_filename.replace("mp4", "mp3")
        audio_size_mb = round(stream.filesize / (1024 * 1024), 2)
        stream.download(output_path=path, filename=file_name, filename_prefix=prefix)
        logger.info(f"{yt.title} descargado correctamente")
        return (True, {"title": yt.title, "size": audio_size_mb})

    except Exception as e:
        print(e)
        return (False, yt.title)


def _downloadPlaylist(url, path):
    error_list = []
    p = Playlist(url)
    for index, url in enumerate(p.video_urls):
        result, data = _downloadAudioFromYouTube(url, path, f"{index+1}. ")
        if not result:
            error_list.append(data["title"])
        print(
            f"{index+1}. {data["title"]} - {Fore.GREEN+('Descargado' if result[0] else Fore.RED+'Error al descargar') + Fore.RESET}"
        )
    return error_list


def _download_any(url: str, path: str):
    try:
        return _downloadAudioFromYouTube(url, path)
    except Exception as e:
        try:
            _downloadPlaylist(url, path)
        except:
            print("No se puede descargar la url seleccionada")
