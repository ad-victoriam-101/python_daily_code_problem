def solution(n, k):
    """
    :param n: int to be converted to binary
    :param k: k-th value of bin(n) to change to a 0 if its a 1.
    :return: an int value, changed by the kth binary value of n
    """
    return n & ~(1 << k-1)


assert solution(37, 3) == 33
