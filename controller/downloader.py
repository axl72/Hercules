from pytube import Playlist, YouTube


def downloadVideo(url, path, index=''):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        file_name = index + stream.default_filename
        stream.download(output_path=path, filename=file_name)

        return (True, yt.title)
    except Exception as e:
        print(e)
        return (False, yt.title)


def downloadPlaylist(url, path):
    error_list = []
    p = Playlist(url)
    for index, url in enumerate(p.video_urls):
        result = downloadVideo(url, path, f"{index+1}. ")
        if(not result[0]):
            error_list.append(result[1])
    return error_list
