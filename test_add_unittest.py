import unittest
import string_calc.add as add_mod


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_mod.add(""), 0)

    def test_add_single_digit(self):
        self.assertEqual(add_mod.add("1"), 1)

    def test_add_multiple_digits(self):
        self.assertEqual(add_mod.add("1,5"), 6)


if __name__ == "__main__":
    unittest.main()
