from tinydb import TinyDB, Query
from pathlib import Path
import os


class DatabaseService:

    def __init__(self, file=""):
        self.file = file
        path = Path(file)
        if not path.exists:
            os.makedirs(os.path.dirname(path))
        self.db = TinyDB(file)

    def add_line(self, line: str):
        self.db.insert(line)

    def remove_line(index: int):
        pass

    def read_all(self):
        return self.db.all()

    def exist(self) -> bool:
        return self.file != ""
