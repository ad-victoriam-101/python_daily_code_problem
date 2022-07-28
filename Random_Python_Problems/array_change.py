def solution(inputArray):
    c = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i + 1]:
            d = inputArray[i] - inputArray[i + 1]
            inputArray[i + 1] += d + 1
            c += d + 1
    return c

    """
    You are given an array of integers. 
    On each move you are allowed to increase exactly one of its element by one. 
    Find the minimal number of moves required to obtain a strictly increasing sequence 
    from the input.
    """