"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """

    def isSymmetric(self, root):
        # Write your code here
        if root == None:
            return True
        return self.isSameNode(root.left, root.right)

    def isSameNode(self, left, right):
        if left == None and right == None:
            return True
        if left != None and right == None:
            return False
        if left == None and right != None:
            return False
        if left.val == right.val:
            return self.isSameNode(left.left, right.right) & self.isSameNode(left.right, right.left)
        else:
            return False