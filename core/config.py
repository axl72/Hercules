from dataclasses import dataclass
import os

USER = os.getlogin()


@dataclass
class Config:
    DOWNLOAD_PATH: str = f"C:/Users/{USER}/Music/Hercules"
    DATABASE_PATH: str = os.path.join(os.getenv("APPDATA"), "Hercules", "mymusic.json")


if __name__ == "__main__":
    config = Config(DOWNLOAD_PATH="hola")
    print(config)
