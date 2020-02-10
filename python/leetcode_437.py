# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root == None:
            return 0
        res = 0
        res = self.findpath(root,sum)

        res = res + self.pathSum(root.left, sum)
        res = res + self.pathSum(root.right, sum)
        return res
    def findpath(self, root, sum):
        if root == None:
            return 0
        res = 0
        if root.val == sum:
            res = res + 1
        res = res + self.findpath(root.left, sum - root.val)
        res = res + self.findpath(root.right, sum - root.val)
        return res