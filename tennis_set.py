def solution(score1, score2):
    high_score = max((score1,score2))
    min_score = min((score1,score2))
    if high_score == 6 and min_score<5:
        return True
    if high_score == 7 and min_score != 7:
        if min_score<5:
            return False
        return True
    return False

assert solution(3,6) == True
assert solution(8,5) == False