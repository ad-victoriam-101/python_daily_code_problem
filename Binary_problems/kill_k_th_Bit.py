def solution(n, k):
    """
    :param n: int to be converted to binary
    :param k: k-th value of bin(n) to change to a 0 if it's a 1.
    :return: an int value, changed by the kth binary value of n
    """
    # x<<y returns x with the bits shifted to the left by y places. and that the ~ is a mask.
    return n & ~(1 << k-1)


assert solution(37, 3) == 33
