"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root node
    @param L: an integer
    @param R: an integer
    @return: the sum
    """

    def rangeSumBST(self, root, L, R):
        # write your code here.

        def dfs(node):
            if node != None:
                if L <= node.val <= R:
                    self.answer = self.answer + node.val
                if L < node.val:
                    dfs(node.left)
                if R > node.val:
                    dfs(node.right)

        self.answer = 0
        dfs(root)
        return self.answer