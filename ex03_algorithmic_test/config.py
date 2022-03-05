'''
I've decided to add larger digits too 
(the ones with underscore in front of the letter) 
so that the code can handle larger numbers
'''
# please keep the digits in descending order
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
NULL_REPRESENTATION = 'nulla'
