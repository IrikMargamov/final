import unittest
import my_module

class TestInfo(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(my_module.int_sum(1, 2), 3)

if __name__ == '__main__':
    unittest.main()