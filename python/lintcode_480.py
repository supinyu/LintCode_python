"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
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
            res.append(str(root.val) + "->" + item)
        for item in right_res:
            res.append(str(root.val) + "->" + item)
        return res