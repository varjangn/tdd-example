import unittest
import string_calc.add as add_mod


class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add_mod.add(""), 0)

    def test_add_single_digit(self):
        self.assertEqual(add_mod.add("1"), 1)

    def test_add_multiple_digits(self):
        self.assertEqual(add_mod.add("1,5"), 6)

    def test_add_newline_char(self):
        self.assertEqual(add_mod.extract_numbers("1\n2,3"), [1,2,3])
        self.assertEqual(add_mod.add("1\n2,3"), 6)

    def test_add_str_with_delimeter(self):
        self.assertEqual(add_mod.extract_delimeter("//;\n1;2"), ';')
        self.assertEqual(add_mod.extract_delimeter("//|\n1|2"), '|')
        self.assertEqual(add_mod.add("//;\n1;2"), 3)


if __name__ == "__main__":
    unittest.main()
