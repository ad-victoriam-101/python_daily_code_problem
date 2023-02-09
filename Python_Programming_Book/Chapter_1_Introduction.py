"""
Chaotic Function an introduction
"""
def main():
    print("This  program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    if x > 1 or x < 0:
        print("please enter a value between 0 and 1")
    for _ in range(10):
        x = 3.9 * x * (1-x)
        print(x)

def notePlay(nums: list[])-> int:
    for i in range(len(nums)):
        if nums[i]%2 == 0:
            nums[i] = 1
        else:
            nums[i] = 0

    return nums
