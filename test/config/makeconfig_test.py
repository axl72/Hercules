import unittest
from config.makeconfig import MakeConfig


class TestMakeconfig(unittest.TestCase):
    def test_read_default_config(self):
        config = MakeConfig.read_config()
        self.assertEqual(config["DOWNLOAD_DIRECTORY"], "C:/Users/Axell/Music/Hercules")


if __name__ == "__main__":
    unittest.main()
