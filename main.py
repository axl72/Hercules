import sys
import os
from controller.downloader import *

if __name__ == "__main__":

    if len(sys.argv) == 1:
        print("Downloader needs a url")
        sys.exit(1)

    dir = Playlist(sys.argv[1]).title

    try:
        path = sys.argv[2] + dir
    except:
        path = './' + dir

    cont = 0
    aux_path = path
    while(os.path.isdir(aux_path)):
        cont += 1
        aux_path = path + f" ({cont})"
    path = aux_path
    os.mkdir(path)

    downloadPlaylist(sys.argv[1], path)
