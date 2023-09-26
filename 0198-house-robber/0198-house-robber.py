class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            aux = second
            second = max(first + nums[i], second)
            first = aux
            
        return second