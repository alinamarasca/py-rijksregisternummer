import unittest
from project import common as c


class TestAreaCodeBe(unittest.TestCase):
    def test_format_area_code_one_digit(self):
        res = c.format_area_code("4")
        self.assertEqual(res, '04')

    def test_format_area_code_two_digits(self):
        res = c.format_area_code("90")
        self.assertEqual(res, '090')

    def test_number_is_in_range(self):
        number = c.select_from_range()
        if number in range(2, 4) or number in range(9, 16) or number in range(19, 20) or number in range(50,
                                                                                                         71) or number in range(
                80, 90):
            res = True
        self.assertTrue(res)

    def test_6_random_digits_if_long_area_code(self):
        res = c.gen_subscriber_number("123")
        self.assertEqual(len(res), 6)

    def test_7_random_digits_if_short_area_code(self):
        res = c.gen_subscriber_number("12")
        self.assertEqual(len(res), 7)