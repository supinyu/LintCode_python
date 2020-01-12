# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if self.ishelp(root) == -1:
            return False
        else:
            return True

    def ishelp(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        left = self.ishelp(root.left)
        right = self.ishelp(root.right)
        if left == -1 or right == -1:
            return -1
        if left - right > 1 or right - left > 1:
            return -1
        else:
            return max(left, right) + 1
