def solution(a, b):
    return sum(bin(x).count('1') for x in range(a, b+1))


assert solution(2,7) == 11