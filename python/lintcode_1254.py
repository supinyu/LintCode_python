# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_sum = 0
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                left_sum = left_sum + root.left.val
        return left_sum + self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left )