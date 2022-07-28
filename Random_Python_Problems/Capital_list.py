def capital_index(string) -> list:
    return [i for i in range(0, len(string)) if string[i].isupper()]


if __name__ == "__main__":
    assert (capital_index("TEsT")) == [0, 1, 3]

# Addin some changes for simplicity.
