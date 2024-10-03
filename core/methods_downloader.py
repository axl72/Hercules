from pytube import Playlist, YouTube
import logging
from colorama import Fore, Back, Style, init

init()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def _downloadVideo(url, path, prefix=""):
    try:
        yt = YouTube(url)
        stream = yt.streams.first()
        filename = stream.default_filename.replace("mp4", "mp3")
        stream.download(output_path=path, filename=filename, filename_prefix=prefix)
        return (True, yt.title)

    except Exception as e:
        print(e)
        return (False, yt.title)


def _downloadAudioFromVideo(url, path, prefix="", callback=None):
    try:
        yt = YouTube(url, on_progress_callback=callback)
        stream = yt.streams.get_audio_only()
        file_name = stream.default_filename.replace("mp4", "mp3")
        audio_size_mb = round(stream.filesize / (1024 * 1024), 2)
        stream.download(output_path=path, filename=file_name, filename_prefix=prefix)
        logger.info(f"{yt.title} descargado correctamente")
        return (True, {"title": yt.title, "size": audio_size_mb})

    except Exception as e:
        print(e)
        return (False, yt.title)


def _downloadPlaylist(url, path, callback):
    error_list = []
    p = Playlist(url)
    for index, url in enumerate(p.video_urls):
        result, data = _downloadAudioFromVideo(url, path, f"{index+1}. ", callback=callback)
        if not result:
            error_list.append(data["title"])
        print(
            f"{index+1}. {data["title"]} - {Fore.GREEN+('Descargado' if result[0] else Fore.RED+'Error al descargar') + Fore.RESET}"
        )
    return error_list


def _download_any(url: str, path: str, callback):
    try:
        return _downloadAudioFromVideo(url, path, callback=callback)
    except Exception as e:
        try:
            _downloadPlaylist(url, path)
        except:
            print("No se puede descargar la url seleccionada")
