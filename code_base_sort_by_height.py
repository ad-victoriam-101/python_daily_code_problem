

def solution(a):
    tree_list = []
    #print(a)
    a_cop = a[:]
    for i,ele in enumerate(a_cop):
       # print(i,ele)
        if ele == -1:
            tree = a[i]
            tree_list.append([tree,i])
    a_no_tree = sorted([x for x in a if x != -1])
    for i in tree_list:
        a_no_tree.insert(i[1],-1)
    return a_no_tree

a= [-1, 150, 190, 170, -1, -1, 160, 180]
print(solution(a))

#better solution.
def better_solution(a):
    l = sorted([i for i in a if i >0])
    for index,number in enumerate(a):
        if number == -1:
            l.insert(number,index)
    return l