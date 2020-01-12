# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        stock = []
        stock.append(root)
        count = 0

        while len(stock) > 0:
            node = stock.pop(0)
            count = count + 1
            if node.left != None:
                stock.append(node.left)
            if node.right != None:
                stock.append(node.right)
        return count