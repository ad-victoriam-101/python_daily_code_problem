import heapq
from random import randint

nums = [randint(1, 101) for i in range(0, 15)]
print(nums)
print(heapq.nlargest(3, nums))
