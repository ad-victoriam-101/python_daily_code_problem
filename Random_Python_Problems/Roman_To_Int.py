# Given a roman numeral return the int value.
# Start by making a dic of vals
roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def roman_to_int(str):
    r_to_i = 0
    for index, numeral in enumerate(str):
        if index < len(str) - 1 and roman_values[numeral] < roman_values[str[index + 1]]:
            r_to_i -= roman_values[numeral]
        else:
            r_to_i += roman_values[numeral]
    return r_to_i


print(roman_to_int('VI'))
print(roman_to_int('XXCI'))
