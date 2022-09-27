#!/bin/python3.9

import sys
import argparse
import os
from controller.downloader import *

parser = argparse.ArgumentParser(description='Process arguments')
parser.add_argument('-u', '--url', type=str, nargs='*', required=True)
parser.add_argument('-d', '--directory', type=str, required=False, default='./')
parser.add_argument('-l', action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.l:
        title = Playlist(args.url[0]).title
        print(title)
        try:
            path = args.directory + title
            print("Directorio donde se descargará la playlist:  ", path)
        except:
            #print(args.directory[0], type(args.directory))
            print("Directorio donde se descargará la playlist:  ", path)
            sys.exit()
        cont = 0
        aux_path = path
        while(os.path.isdir(aux_path)):
            cont += 1
            aux_path = path + f" ({cont})"
        path = aux_path
        os.mkdir(path)

        error_list = downloadPlaylist(args.url[0], path)

    else:
        print("Hola")
        title = YouTube(args.url[0]).title
        try:
            path = args.directory + title
        except:
            sys.exit()

        downloadVideo(args.url[0], path)
