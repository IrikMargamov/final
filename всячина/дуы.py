import unittest
from info import parse_info

class TestInfo(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse_info("Ivan", "Ivanov", "22.06.1998"), ("Ivan", "Ivanov", "22.06.1998"))

    def test_simple(self):
        self.assertEqual(parse_info("ivan", "Ivanov", "22.06.1998"), ("Ivan", "Ivanov", "22.06.1998"))

    def test_simple(self):
        self.assertEqual(parse_info("ivan", "Ivanov", "22.06.1998"), ("Ivan", "Ivanov", "22.06.1998"))

if __name__ == '__main__':
    unittest.main()