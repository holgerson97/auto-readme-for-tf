import unittest
from filecmp import cmp
from os import system

class TestRender(unittest.TestCase):

    def test_file(self):
        system('./main.py')
        self.assertTrue(cmp('../tests/samples/README.md', '../tests/README.md'), "The to files aren't identical.")

if __name__ == '__main__':
    unittest.main() 