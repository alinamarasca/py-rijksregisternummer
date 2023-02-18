import re
import unittest
from unittest import mock

import functions as c


class TestCalcISNZrightFormat(unittest.TestCase):
    res = c.calc_isnz()

    @mock.patch('module_under_test.input', create=True)
    def test_is_numeric(self, res):
        no_punctuation = re.sub(r'[^\w\s]', '', res)
        self.assertTrue(no_punctuation.isnumeric())

    def test_has_2_blocks_separated_with_dash(self, res):
        blocks = res.split("-")
        self.assertEqual(len(blocks), 2)

    def test_first_block_has_3_parts_separated_with_periods(self, res):
        fb = res.split("-")[0]
        li = fb.split(".")
        self.assertEqual(len(li), 3)

    def test_first_block_each_part_has_2_chars(self, res):
        fb = res.split("-")[0]
        li = fb.split(".")
        for item in li:
            self.assertEqual(len(item), 2)

    def test_second_block_has_2_parts_separated_with_periods(self, res):
        fb = res.split("-")[1]
        li = fb.split(".")
        self.assertEqual(len(li), 2)

    def test_second_block_1_part_has_3_chars(self, res):
        fb = res.split("-")[0]
        li = fb.split(".")
        self.assertEqual(len(li[0]), 3)

    def test_second_block_1_part_has_2_chars(self, res):
        fb = res.split("-")[0]
        li = fb.split(".")
        self.assertEqual(len(li[1]), 2)


if __name__ == "__main__":
    unittest.main()
