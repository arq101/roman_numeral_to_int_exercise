# -*- coding: utf-8 -*-

ROMAN_SYMBOLS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def _check_if_roman_numerals_are_invalid(numeral_str):
    """
    Returns True if a character from the function argument is not from the
    valid Roman numeral symbols.
    """
    return True \
        if [char for char in set(numeral_str) if char not in ROMAN_SYMBOLS.keys()] \
        else False


def roman_numeral_to_int(roman_num_str):
    if _check_if_roman_numerals_are_invalid(roman_num_str):
        return
    else:
        result = 0
        i = 0

        # process the last item in the string later on
        while i < len(roman_num_str) - 1:

            if roman_num_str[i] == 'I':
                if roman_num_str[i+1] in {'V', 'X'}:
                    result -= ROMAN_SYMBOLS['I']
                else:
                    result += ROMAN_SYMBOLS['I']

            elif roman_num_str[i] == 'X':
                if roman_num_str[i+1] in {'L', 'C'}:
                    result -= ROMAN_SYMBOLS['X']
                else:
                    result += ROMAN_SYMBOLS['X']

            elif roman_num_str[i] == 'C':
                if roman_num_str[i+1] in {'D', 'M'}:
                    result -= ROMAN_SYMBOLS['C']
                else:
                    result += ROMAN_SYMBOLS['C']

            else:
                result += ROMAN_SYMBOLS[roman_num_str[i]]

            i += 1

        result += ROMAN_SYMBOLS[roman_num_str[-1]]
        return result

