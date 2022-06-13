class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ##time complexity, O(n) Space complexity O(n)

    def tree_to_list(self, root: TreeNode, arr: list):
        # func to return a list of all values in a given BinaryTree(BT)
        if not root:
            # null pretection.
            return arr
        self.tree_to_list(root.left, arr)
        arr.append(root.val)
        self.tree_to_list(root.right, arr)
        return arr

    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        arr1 = []
        arr2 = self.tree_to_list(root, arr1)
        print(arr2)
        start = 0
        end = len(arr2) - 1
        while start < end:
            if arr2[start] + arr2[end] == target:
                return True
            if arr2[start] + arr2[end] > target:
                end -= 1
            if arr2[start] + arr2[end] < target:
                start += 1
        return False
