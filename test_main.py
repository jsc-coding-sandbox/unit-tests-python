import unittest

import main


class TestMain(unittest.TestCase):

    def test_add_two(self):
        self.assertEqual(main.add_two(1,2), 3, "Should be 3")

    def test_sub_two(self):
        self.assertEqual(main.sub_two(2,1), 1, "Should be 1")

    def test_div_two(self):
        self.assertEqual(main.div_two(2,2), 1, "Should be 1")

    def test_printeger(self):
        self.assertEqual(main.printeger(1), "1", "Should be 1")


if __name__ == "__main__":
    unittest.main()

