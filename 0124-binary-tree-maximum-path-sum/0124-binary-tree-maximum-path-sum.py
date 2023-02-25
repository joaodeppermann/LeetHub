# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxSum = -inf
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def max_gain(node):
            if not node:
                return 0
            # max sum between the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            # sum where the current node is the spliting node
            sum_newpath = node.val + left_gain + right_gain
            # update max_sum if it's better to use current node as spliting node
            self.maxSum = max(self.maxSum, sum_newpath)
            # return max val for this node without spliting 
            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return self.maxSum
            