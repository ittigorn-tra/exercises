from operator import indexOf

ROMAN_DIGITS = ["_V", "_I_V", "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
ARABIC_DIGITS = [5000, 4000, 1000, 900, 500,  400, 100,  90,  50,  40,  10,   9,  5,   4,  1]


def to_roman_digits(value: int) -> str:
    if not isinstance(value, int):
        raise ValueError('"value" must be int')
    if value < 0:
        raise ValueError('Roman Numerals does not include negative numbers')
    if value == 0:
        return 'nulla'

    start_at = 0
    result = []

    # loop while not depleted
    while value > 0:
        for arabic_digit in ARABIC_DIGITS[start_at:]:
            # find value that subtract to zero, or more than 0, descending
            if (value - arabic_digit == 0) or ((value - arabic_digit) > 0):
                digit_idx = indexOf(ARABIC_DIGITS, arabic_digit)
                result.append(ROMAN_DIGITS[digit_idx])
                start_at = digit_idx
                value = value - arabic_digit
                break

    return ''.join(result)


if __name__ == '__main__':
    value = 0

    result = to_roman_digits(value=value)
    print(result)
