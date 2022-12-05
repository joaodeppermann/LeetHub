# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        self.ans = None
        def dfs(node):
            if not node:
                return False
            
            l = dfs(node.left)
            r = dfs(node.right)
            cur = node == p or node == q
            
            if (l and r) or (r and cur) or (l and cur):
                self.ans = node
            
            return l or r or cur
        dfs(root)
        return self.ans
        