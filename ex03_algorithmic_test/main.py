from config import ARABIC_ROMAN_DIGIT_MAP, NULL_REPRESENTATION


def to_roman_digits(value: int) -> str:
    if not isinstance(value, int):
        raise ValueError('"value" must be int')
    if value < 0:
        raise ValueError('Roman Numerals does not include negative numbers')
    if value == 0:
        return NULL_REPRESENTATION

    start_at = 0
    result = []

    # loop while not depleted
    while value > 0:
        for digit_pair in ARABIC_ROMAN_DIGIT_MAP[start_at:]:
            # find value that subtract to zero, or more than 0, descending
            if (value - digit_pair['arabic']) >= 0:
                result.append(digit_pair['roman'])
                value = value - digit_pair['arabic']
                break
            else:
                start_at += 1

    return ''.join(result)


if __name__ == '__main__':
    value = 2253

    result = to_roman_digits(value=value)
    print(result)
