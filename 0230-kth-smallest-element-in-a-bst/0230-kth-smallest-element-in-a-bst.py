# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 1
        stack = []
        while stack or root:
            # go as far as you can to the left
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if count == k:
                return root.val
            count += 1
            root = root.right