from dataclasses import dataclass
import os

USER = os.getlogin()

@dataclass
class Config():
    DOWNLOAD_PATH:str = f"C:/Users/{USER}/Music/Hercules"