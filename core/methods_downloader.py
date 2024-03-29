from pytube import Playlist, YouTube
import logging
from colorama import Fore, Back, Style, init
init()

logging.basicConfig(level=logging.INFO)           
logger = logging.getLogger()


def _downloadVideo(url, path, prefix=''):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        file_name = stream.default_filename.replace('mp4', 'mp3')
        stream.download(output_path=path, filename=file_name,
                        filename_prefix=prefix)
        logger.info(f'{yt.title} descargado correctamente')
        return (True, yt.title)

    except Exception as e:
        print(e)
        return (False, yt.title)


def _downloadPlaylist(url, path):
    error_list = []
    p = Playlist(url)
    for index, url in enumerate(p.video_urls):
        result = _downloadVideo(url, path, f'{index+1}. ')
        if(not result[0]):
            error_list.append(result[1])
        print(f"{index+1}. {result[1]} - {Fore.GREEN+('Descargado' if result[0] else Fore.RED+'Error al descargar') + Fore.RESET}")
    return error_list


def _download_any(url:str, path:str):
    try:
        _downloadVideo(url, path)
    except Exception as e:
        try:
            _downloadPlaylist(url, path)
        except:
            print("No se puede descargar la url seleccionada")

