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
