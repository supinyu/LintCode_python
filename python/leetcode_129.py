# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        result = self.binaryTreePaths(root)
        total_sum = 0
        for item in result:
            item = item.lstrip("0")
            if len(item) == 0:
                item = 0
            else:
                item = int(item)
            total_sum = total_sum + item
        return total_sum


    def binaryTreePaths(self, root):
        # write your code here
        if root == None:
            return []
        res = []
        if root.left == None and root.right == None:
            res.append(str(root.val))
            return res
        left_res = self.binaryTreePaths(root.left)
        right_res = self.binaryTreePaths(root.right)
        for item in left_res:
            res.append(str(root.val) + item)
        for item in right_res:
            res.append(str(root.val) + item)
        return res