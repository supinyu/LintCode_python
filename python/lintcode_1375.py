# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, sum):
        # Write your code here.
        if root == None:
            return []
        res = []
        sum = sum - root.val
        if root.left == None and root.right == None and sum == 0:
            res.append([root.val])
            return res
        left_res = self.pathSum(root.left, sum)
        right_res = self.pathSum(root.right, sum)
        for item in left_res:
            item.insert(0, root.val)
            res.append(item)
        for item in right_res:
            item.insert(0, root.val)
            res.append(item)
        return res



# DFS solution


class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, sum):
        # Write your code here.
        result = []
        if root == None:
            return result
        self.dfs(root, sum,[], result)
        return result
    def dfs(self, root, target ,path, result):
        if root == None:
            return
        path.append(root.val)
        target = target - root.val
        if target == 0 and root.left == None and root.right == None:
            result.append(list(path))
        self.dfs(root.left , target, path, result)
        self.dfs(root.right, target, path, result)
        path.pop()

        return