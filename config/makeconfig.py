import json

CONFIG_PATH = "./args.conf"

class MakeConfig:

    def read_config():
        file = open(CONFIG_PATH, 'r')

        args = json.load(file)
        print(args)
