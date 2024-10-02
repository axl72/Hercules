from dataclasses import dataclass
import os

USER = os.getlogin()


@dataclass
class Config:
    DOWNLOAD_PATH: str = f"C:/Users/{USER}/Music/Hercules"


if __name__ == "__main__":
    config = Config(DOWNLOAD_PATH="hola")
    print(config)
