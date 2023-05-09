class Solution:
    def rob(self, nums: List[int]) -> int:
        # edge case
        if len(nums) == 1:
            return nums[0]
        
        # dp = [prev, cur]
        dp = [0, 0] 
        
        for i in range(len(nums)):
            tmp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1]) 
            dp[0] = tmp
            
        return dp[1]