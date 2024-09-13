import json
import os

CONFIG_PATH = "./args.conf"


class MakeConfig:
    config = None

    @staticmethod
    def read_config():
        try:
            with open(CONFIG_PATH, "r") as config_file:
                MakeConfig.config = json.load(config_file)
                MakeConfig.__make_download_directory__()
                return MakeConfig.config

        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print(e)

    @staticmethod
    def __make_download_directory__():
        username = os.getlogin()
        directory = str(MakeConfig.config["DOWNLOAD_DIRECTORY"])
        directory = directory.replace("$USER", username)
        MakeConfig.config["DOWNLOAD_DIRECTORY"] = directory


if __name__ == "__main__":
    print(MakeConfig.read_config())
