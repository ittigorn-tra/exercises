from logging import getLogger

import pytest
from config import NULL_REPRESENTATION
from main import to_roman_digits

logger = getLogger()


@pytest.fixture
def good_values():
    return [
        [0, NULL_REPRESENTATION],
        [1, 'I'],
        [4, 'IV'],
        [9, 'IX'],
        [10, 'X'],
        [11, 'XI'],
        [21, 'XXI'],
        [40, 'XL'],
        [2253, 'MMCCLIII'],
        [361054, '_C_C_C_L_XMLIV'],
        [667189, '_D_C_L_X_VMMCLXXXIX'],
        [285667, '_C_C_L_X_X_X_VDCLXVII'],
        [126266, '_C_X_X_VMCCLXVI'],
        [188051, '_C_L_X_X_X_VMMMLI'],
        [445782, '_C_D_X_L_VDCCLXXXII'],
        [162972, '_C_L_XMMCMLXXII'],
        [660787, '_D_C_L_XDCCLXXXVII'],
        [64455, '_L_X_I_VCDLV'],
        [91430, '_X_CMCDXXX'],
    ]


@pytest.fixture
def bad_values():
    return [
        -1,
        -10,
        -123,
        -59342
    ]


@pytest.fixture
def zero_value():
    return 0


def test_good_values(good_values):
    for value, expected_result in good_values:
        roman_digits = to_roman_digits(value)
        logger.info(f'Test Value : {str(value).rjust(8)} Roman Digits : {roman_digits}')

        # check if return type is as in the requirement
        assert isinstance(roman_digits, str)
        assert len(roman_digits) > 0
        assert roman_digits == expected_result


def test_bad_values(bad_values):
    for value in bad_values:
        logger.info(f'Test Value : {str(value).rjust(5)}')
        with pytest.raises(ValueError):
            to_roman_digits(value)
