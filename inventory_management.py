def solution(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    else:
        # max takes two values or an iterable and returns the max value.
        # in this case, using one liners we can traverse the if else in a more confined box. 

        return max(value1 if weight1 <= maxW else 0, value2 if weight2 <= maxW else 0)


assert (solution(10, 5, 6, 4, 8) == 10)
