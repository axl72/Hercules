from pytube import Playlist, YouTube
import time
import traceback
import os
import logging
from colorama import Fore, Back, Style, init
from pathlib import Path
import tempfile
from moviepy.editor import VideoFileClip, AudioFileClip
from util.dirs import make_temp_name
import uuid

init()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def _downloadVideoFromYouTube(
    url: str, path: Path, resolution: str, prefix: str = ""
) -> tuple[bool, dict]:
    try:
        yt = YouTube(url)
        progressive_stream = yt.streams.filter(res=resolution, progressive=True)
        adaptative_stream = yt.streams.filter(res=resolution, adaptive=True)

        if progressive_stream:
            stream = progressive_stream.first()
            filename = stream.default_filename.split(".")[0] + f" {resolution}" + ".mp4"
            size_mb = round(stream.filesize / (1024 * 1024), 2)
            stream.download(output_path=path, filename=filename, filename_prefix=prefix)
            return (True, {"title": yt.title, "size": size_mb})
        elif adaptative_stream:
            stream = adaptative_stream.first()
            filename = stream.default_filename.split(".")[0] + f" {resolution}" + ".mp4"
            print("Descargando video adaptative")
            tempdir = tempfile.mktemp()
            print(f"Descargando video en: {tempdir}")
            video_name = str(uuid.uuid1())
            temp_video_path = os.path.join(tempdir, video_name)
            stream.download(output_path=tempdir, filename=video_name)
            video = VideoFileClip(temp_video_path)
            audio_name = str(uuid.uuid1())
            temp_audio_path = os.path.join(tempdir, audio_name)
            print("Descargando audio")
            yt.streams.get_audio_only().download(
                output_path=tempdir, filename=audio_name
            )
            audio_stream = os.path.join(tempdir, audio_name)
            audio = AudioFileClip(audio_stream)

            video_with_audio = video.set_audio(audio)

            print(f"Guardando el video final en: {path}")
            # Guardar el nuevo video con audio combinado
            video_with_audio_path = os.path.join(path, filename)
            video_with_audio.write_videofile(
                video_with_audio_path, codec="libx264", audio_codec="aac"
            )
            size_mb = round(os.path.getsize(video_with_audio_path) / (1024 * 1024), 2)

            video.close()
            audio.close()
            os.remove(temp_video_path)
            os.remove(temp_audio_path)

            return (True, {"title": yt.title, "size": size_mb})
    except TypeError as e:
        print(e)
        return (False, yt.title)

    except Exception as e:
        print(traceback.format_exc())
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
