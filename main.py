#!/bin/python3.9

import sys
import argparse
import os
from core.downloader import Downloader
from tkinter.filedialog import askdirectory
from colorama import Fore, Back, Style, init
from pytube import Playlist, YouTube
from view.Menu import MainWindow
from controller.downloader_controller import DownloaderController

# Inicialización de colorama
init()

parser = argparse.ArgumentParser(description="Process arguments")
parser.add_argument("-u", "--url", type=str, nargs="*", required=True)
parser.add_argument("-d", "--directory", type=str, required=False, default=askdirectory)
parser.add_argument("-l", action="store_true")

if __name__ == "__main__":
    view = MainWindow()
    controller = DownloaderController(view)
    controller.run()
