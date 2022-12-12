class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range(len(nums) - 2):
            myhash = set()
            targetSum = -1*nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] in myhash:
                    res.add(tuple(sorted([nums[j], nums[i], targetSum - nums[j]])))
                else:
                    myhash.add(targetSum - nums[j])
        return res
        
        
        
        
        
        
        
        
        
        