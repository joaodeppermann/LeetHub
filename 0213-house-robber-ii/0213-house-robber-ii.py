class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) == 1:
            return nums[0]
        
        # If you rob the first you cannot rob the last one 
        # Try to rob with first house included 
        dp = [0,0] # previous, current house
        for i in range(len(nums) - 1):
            aux = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = aux
        first = dp[1]
        
        # Rob excluding first and including last
        dp = [0,0] # previous, current house
        for i in range(1, len(nums)):
            aux = dp[1]
            dp[1] = max(dp[0] + nums[i], dp[1])
            dp[0] = aux
        second = dp[1]
        
        return max(first, second)