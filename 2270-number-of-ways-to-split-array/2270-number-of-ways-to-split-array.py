# class Solution:
#     def waysToSplitArray(self, nums: List[int]) -> int:
#         prefix_sum = [nums[0]]*len(nums)
#         for i in range(1, len(nums)):
#             prefix_sum[i] = prefix_sum[i - 1] + nums[i]
#         res = 0
#         for i in range(len(nums) - 1):
#             leftSum = prefix_sum[i]
#             rightSum = prefix_sum[len(nums) - 1] - leftSum
#             if leftSum >= rightSum:
#                 res += 1
#         return res
    
    
# Can we do any better?

# In terms of time: NO. We will need to traverse the array atleast once (at any cost, in any situation).
# In terms of space: YES. We actually do not need a complete prefix array.
# Let's see how!

# We just need to have two sum variables storing the sum of left part and right part.
# Initially, the left part will contain the first element and right part will contain sum of array - the first element.
# As we increment the index, we take the current nums[i] value and add it to the left part and remove it from the right part.

# Hence reducing the space complexity to O(1).

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        leftSum, rightSum = 0, 0
        res = 0
        n = len(nums)
        for i in range(n - 1):
            leftSum += nums[i]
            rightSum = totalSum - leftSum
            if leftSum >= rightSum:
                res += 1
        return res