import unittest
from project import common as c


class TestFormatDateOfBirth(unittest.TestCase):
    def test_returns_inverted_list(self):
        res = c.formatDateOfBirth("10/11/1985")
        self.assertEqual(res, ['85', '11', '10'])


class TestExtractYear(unittest.TestCase):
    def test_returns_two_last_numbers(self):
        res = c.extractYear("1976")
        self.assertEqual(res, '76')


class TestCalcSecondBlock(unittest.TestCase):
    def test_return_odd_number_if_a(self):
        res = c.calc_second_block("a") % 2
        self.assertEqual(res, 1)

    def test_if_a_generates_3digits_number(self):
        res = str(c.calc_second_block("a"))
        self.assertEqual(len([*res]), 3)

    def test_even_even_number_if_b(self):
        res = c.calc_second_block("b") % 2
        self.assertEqual(res, 0)

    def test_if_b_generates_3digits_number(self):
        res = str(c.calc_second_block("b"))
        self.assertEqual(len([*res]), 3)

    def test_error_message_if_not_a_or_b(self):
        res = c.calc_second_block("c")
        self.assertEqual(res, "Error: wrong data")


class TestConcat2IfMoreThan2000(unittest.TestCase):
    def test_if_year_equals_2000_concat_2(self):
        res = c.concat_2_if_more_than_2000("220420111", 2022)
        self.assertEqual(res, "2")

    def test_if_year_more_than_2000_concat_2(self):
        res = c.concat_2_if_more_than_2000("000317534", 2000)
        self.assertEqual(res, 24)

    def test_if_year_less_than_2000_not_concat_2(self):
        res = c.concat_2_if_more_than_2000("561220765", 1956)
        self.assertEqual(res, 89)

class TestCheckDateInputFormat(unittest.TestCase):
    def test_detects_incorrect_input(self):
        res = c.check_date_input_format("20.12.1987")
        self.assertEqual(res, "2")


if __name__ == "__main__":
    unittest.main()
