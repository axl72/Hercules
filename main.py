import youtube_dl


def main():
    url = input("Ingresa la url: ")
    try:
        video_info = youtube_dl.YoutubeDL().extract_info(
            url=url, download=False
        )
        filename = "%(title)s.%(exts)s"
        option = {
            'writethumbnail': True,
            'format': 'bestaudio/best',
            'keepvideo': False,
            'outtmpl': "/songs/" + filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }, {'key': 'EmbedThumbnail'}]
        }
        with youtube_dl.YoutubeDL(option) as ydl:
            ydl.download((url,))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
