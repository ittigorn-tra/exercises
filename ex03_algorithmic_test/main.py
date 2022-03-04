ARABIC_ROMAN_DIGIT_MAP = [
    {"arabic": 1000000, "roman": "_M"},
    {"arabic": 900000, "roman": "_C_M"},
    {"arabic": 500000, "roman": "_D"},
    {"arabic": 400000, "roman": "_C_D"},
    {"arabic": 100000, "roman": "_C"},
    {"arabic": 90000, "roman": "_X_C"},
    {"arabic": 50000, "roman": "_L"},
    {"arabic": 40000, "roman": "_X_L"},
    {"arabic": 10000, "roman": "_X"},
    {"arabic": 9000, "roman": "_I_X"},
    {"arabic": 5000, "roman": "_V"},
    {"arabic": 5000, "roman": "_V"},
    {"arabic": 4000, "roman": "_I_V"},
    {"arabic": 1000, "roman": "M"},
    {"arabic": 900, "roman": "CM"},
    {"arabic": 500, "roman": "D"},
    {"arabic": 400, "roman": "CD"},
    {"arabic": 100, "roman": "C"},
    {"arabic": 90, "roman": "XC"},
    {"arabic": 50, "roman": "L"},
    {"arabic": 40, "roman": "XL"},
    {"arabic": 10, "roman": "X"},
    {"arabic": 9, "roman": "IX"},
    {"arabic": 5, "roman": "V"},
    {"arabic": 4, "roman": "IV"},
    {"arabic": 1, "roman": "I"},
]


def to_roman_digits(value: int) -> str:
    if not isinstance(value, int):
        raise ValueError('"value" must be int')
    if value < 0:
        raise ValueError('Roman Numerals does not include negative numbers')
    if value == 0:
        return 'nulla'

    result = []

    # loop while not depleted
    while value > 0:
        for digit_pair in ARABIC_ROMAN_DIGIT_MAP:
            # find value that subtract to zero, or more than 0, descending
            if (value - digit_pair['arabic']) >= 0:
                result.append(digit_pair['roman'])
                value = value - digit_pair['arabic']
                break

    return ''.join(result)


if __name__ == '__main__':
    value = 11000

    result = to_roman_digits(value=value)
    print(result)
