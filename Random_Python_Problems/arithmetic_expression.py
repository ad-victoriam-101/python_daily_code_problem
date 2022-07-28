def solution(a,b,c):
    """
    Consider an arithmetic expression of the form a#b=c. 
    Check whether it is possible to replace # with one of the four signs: +, -, * or / 
    to obtain a correct expression.

    Args:
        a (int): such that 1<=a<=20
        b (int): such that 1<=b<=20
        c (int): such that 1<=c<=20
    """
    return c in (a+b,a-b,a*b,a/b)

#unit test

assert solution(8,2,4) == True

assert solution(8,3,2) == False