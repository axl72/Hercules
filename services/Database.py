from tinydb import TinyDB, Query
from pathlib import Path


class DatabaseService:

    def __init__(self, file):
        self.db = TinyDB(file)

    def add_line(self, line: str):
        self.db.insert(line)

    def remove_line(index: int):
        pass

    def read_all(self):
        return self.db.all()
