# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        value = float('-inf')
        def dfs(node):
            nonlocal value
            if not node:
                return 0
            leftMaxPathSum = max(0, dfs(node.left))
            rightMaxPathSum = max(0, dfs(node.right))
            value = max(value, (leftMaxPathSum + node.val + rightMaxPathSum))
            return node.val + max(leftMaxPathSum, rightMaxPathSum)
        dfs(root)
        return value