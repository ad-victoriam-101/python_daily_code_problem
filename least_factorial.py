def solution(n):
    k = 1
    if n == 1:
        return 1
    while math.factorial(k)<n:
        k+=1
    return math.factorial(k)

assert solution(17)==24