import collections

deque_colors = collections.deque(["red", "green", "white"])
print(deque_colors)
# append to the left.
deque_colors.appendleft("pink")
print(deque_colors)
# append to the right
deque_colors.append("orange")
print(deque_colors)
# pip from the right
deque_colors.pop()
print(deque_colors)
# pop from the left
deque_colors.popleft()
print(deque_colors)
# reverse the order
deque_colors.reverse()
print(deque_colors)


def internal_deque(li, rev = False):
    pass