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


class TestCalcFinalNumber(unittest.TestCase):
    def test_calc_final_number(self):
        res = c.calc_final_number("871220434")
        self.assertEqual(res, "4")


class TestCheckDateInputFormat(unittest.TestCase):
    def test_detects_incorrect_input(self):
        res = c.check_date_input_format("20.12.1987")
        self.assertEqual(res, False)

class TestMakeThreeDigitsNumber(unittest.TestCase):
    def test_adds_zeros_to_have_3_chars(self):
        res = c.concat_zero_for_three_chars(2)
        self.assertEqual(len(res), 3)

    def test_adds_zeros_to_have_3_chars(self):
        res = c.concat_zero_for_three_chars(10)
        self.assertEqual(len(res), 3)

    def test_adds_zeros_to_have_3_chars(self):
        res = c.concat_zero_for_three_chars(99)
        self.assertEqual(len(res), 3)

if __name__ == "__main__":
    unittest.main()
