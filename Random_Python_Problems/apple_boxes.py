def solution(k):
    list_k = [i for i in range(1, k+1)]
    even_nums = list_k[::2]
    odd_nums = list_k[1::2]
    even_sum = sum([i*i for i in even_nums])
    odd_sum = sum([i*i for i in odd_nums])
    #print(even_nums, even_sum, odd_nums, odd_sum)
    return odd_sum-even_sum
    
print(solution(5))
assert solution(5) == -15

