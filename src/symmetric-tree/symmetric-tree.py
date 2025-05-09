def dfs(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False
    return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return dfs(root.left, root.right)
        