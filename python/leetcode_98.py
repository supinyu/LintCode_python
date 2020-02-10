# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def help(root, left = float('-inf'), right = float('inf')):
            if root == None:
                return True
            if root.val <= left or root.val >= right:
                return False
            if not help(root.left, left, root.val):
                return False
            if not help(root.right, root.val, right ):
                return False
            return True
        return help(root)