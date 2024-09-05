import unittest
from services.Database import DatabaseService
import os


class TestDataBaseService(unittest.TestCase):
    def test_write_data_in_database(self):
        path = "mymusic_test.json"
        db = DatabaseService(path)
        data = {
            "title": "When I write my master thesys",
            "size": "3.33 Mb",
            "url": "https://www.youtube.com/watch?v=RwSjL7nluwQ",
            "path_saved": "C:\\Users\\Axell\\Music\\Hercules",
        }
        db.add_line(data)

        registers = db.read_all()

        self.assertEqual([data], registers)

    def tearDown(self):
        os.remove("mymusic_test.json")


if __name__ == "__main__":
    unittest.main()
