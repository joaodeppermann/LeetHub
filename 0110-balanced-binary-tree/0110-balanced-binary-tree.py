# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return True
            if abs(self.getHeight(node.left) - self.getHeight(node.right)) > 1:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)
        
    def getHeight(self, node):
        if not node:
            return -1
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return max(left, right) + 1