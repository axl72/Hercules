import sys
import os
from controller.downloader import *

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Hercules needs a url")
        sys.exit(1)

    title = Playlist(sys.argv[1]).title

    try:
        path = sys.argv[2] + "/" + title
    except:
        path = './' + title

    cont = 0
    aux_path = path
    while(os.path.isdir(aux_path)):
        cont += 1
        aux_path = path + f" ({cont})"
    path = aux_path
    os.mkdir(path)

    error_list = downloadPlaylist(sys.argv[1], path)
