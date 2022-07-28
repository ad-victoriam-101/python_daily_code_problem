def solution(a):
    team_1 = []
    team_2 = []
    for index in range(len(a)):
        if index % 2 == 0:
            team_1.append(a[index])
        else:
            team_2.append(a[index])
    return [sum(team_1),sum(team_2)]
#better solution
def solution(a):
    return [sum(a[::2]),sum(a[1::2])]