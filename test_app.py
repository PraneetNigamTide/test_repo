import unittest
from src.app import add

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8, 'Should be 8')

if __name__ == '__main__':
    unittest.main()