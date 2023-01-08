class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = []
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefixSum.append(total)
            
        return prefixSum