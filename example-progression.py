from pytube import YouTube
import pytube.request

pytube.request.default_range_size = 300000  # 1 MB chunk size


def SHOW(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print("porcentaje de completación: ", percentage_of_completion)


video_url = "https://www.youtube.com/watch?v=_Jcz454kpp8"

object_video = YouTube(video_url, on_progress_callback=SHOW)

Data_streams = object_video.streams

desiered_stream = Data_streams.get_highest_resolution()

print(desiered_stream.filesize)

desiered_stream.download(output_path=r"./", filename="VIDEO.mp4")

print("Download commpleted")
