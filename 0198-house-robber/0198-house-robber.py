class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0, 0] # prev, cur
        for n in nums:
            # Steal the current house or keep the value from the previous house
            aux = dp[1]
            dp[1] = max(n + dp[0], dp[1])
            dp[0] = aux
        return dp[1]