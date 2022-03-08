def solution(inputArray):
    """
    Given an array of integers, find the maximal absolute difference between any two of its adjacent elements.
    :param inputArray: array of integers
    :return: max absolute difference of two elements
    """
    current_max = 0
    for i in range(len(inputArray)-1):
        compare = abs(inputArray[i]-inputArray[i+1])
        if compare > current_max:
            current_max = compare
    return current_max
def solution2(a):
    return max([abs(a[i]-a[i+1]) for i in range(len(a))])

assert solution([2,4,1,0]) == 3
