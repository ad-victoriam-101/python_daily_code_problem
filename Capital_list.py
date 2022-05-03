def capital_index(string) -> list:
    return [i for i in range(0, len(string)) if string[i].isupper()]


print(capital_index("TEsT"))