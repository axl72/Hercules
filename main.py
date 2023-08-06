#!/bin/python3.9

import sys
import argparse
import os
from controller.downloader import *
from tkinter.filedialog import askdirectory
from colorama import Fore, Back, Style, init

# Inicialización de colorama
init()

parser = argparse.ArgumentParser(description='Process arguments')
parser.add_argument('-u', '--url', type=str, nargs='*', required=True)
parser.add_argument('-d', '--directory', type=str, required=False, default=askdirectory())
parser.add_argument('-l', action='store_true')

if __name__ == "__main__":
    args = parser.parse_args()

    if args.l:
        title = Playlist(args.url[0]).title
        print(title)
        try:
            path = args.directory
            if path == "":
                print(f"{Fore.YELLOW}Descarga cancelada{Fore.RESET}")
                raise Exception("Ningún directorio fue seleccionado")


            print(f"{Fore.CYAN}Directorio donde se descargará la playlist:  {path}{Fore.RESET}")
        except:
            #print(args.directory[0], type(args.directory))
            print("Directorio donde se descargará la playlist:  ", path)
            sys.exit()
        error_list = downloadPlaylist(args.url[0], path)
        print(f"{Fore.BLUE}Descarga terminada exitosamente{Fore.RESET}")

    else:
        title = YouTube(args.url[0]).title
        try:
            path = args.directory + title
        except:
            sys.exit()

        estate, title = downloadVideo(args.url[0], path)
