def unique_in_list(l1, l2):
    """
    check each value in l1, test if it exists in l2.
    list comp for union
    O(n*m)
    """

    return_list = []
    list_comp = [i for i in l1 if i in l2]
    for char in l1:
        if char in l2:
            return_list.append(char)
    return return_list


def unique_counter(l1, l2):
    """
    return sorted by value dict that contians unique union of two lists.
    """
    # python Counter

    # first make a list of common values in both lists.
    union_lists = unique_in_list(l1, l2)
    stonks_dict = sorted({k: 1 for k in union_lists})

    def dict_counter(li):
        for char in li:
            if char in stonks_dict:
                stonks_dict.char += 1

    dict_counter(l1)
    dict_counter(l2)
    stonks_dict = sorted(stonks_dict, key=lambda: stonks_dict.char)

    return stonks_dict.keys