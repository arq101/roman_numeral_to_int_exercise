#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from roman_numeral_converter import roman_numeral_to_int


class TestRomanNumeralToInteger(unittest.TestCase):

    def test_invalid_roman_symbols(self):
        self.assertIsNone(roman_numeral_to_int('XIF'))

    def test_with_positive_notation(self):
        self.assertEqual(roman_numeral_to_int('MLXVI'), 1066)

    def test_with_negative_notation(self):
        self.assertEqual(roman_numeral_to_int('MCMIV'), 1904)

    def test_with_incorrect_use_of_symbols(self):
        self.assertEqual(roman_numeral_to_int('IXX'), 19)
        self.assertEqual(roman_numeral_to_int('XIX'), 19)


if __name__ == '__main__':
    unittest.main(verbosity=2)
