def solution(param1, param2, ):
    """
    given two numbers add each digit, and return the non remainder
    ex: For param1 = 456 and param2 = 1734, the output should be
        solution(param1, param2) = 1180.
    :param param1: int, between 0 and 10,000
    :param param2: int, between 0 and 10,000
    :return: int, of max length.
    """
    # start by converting the provided ints to justified strings with 0's

    str_param1 = str(param1).zfill(max(len(str(param1)), len(str(param2))))
    str_param2 = str(param2).zfill(max(len(str(param1)), len(str(param2))))
    # uncomment to check if zfilled propperly
    # print(str_param1, str_param2)
    return_string = ''
    #since strings are the same len now we can itterate though each index
    for i in range(0, len(str_param2)):
        #make int for each, addition
        carry_int = int(str_param1[i]) + int(str_param2[i])
        # remember that % 10 in python will return the last digit of any int.
        return_string += str(carry_int % 10)
    return int(return_string)


print(solution(456, 1734))

assert solution(456, 1734) == 1180
