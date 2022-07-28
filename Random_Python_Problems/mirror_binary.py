def solution(a):
    binary = format(a,'b')
    binary = binary[::-1]
    return int(binary,2)