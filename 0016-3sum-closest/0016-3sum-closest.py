class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        curMinDiff = +inf
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = nums[l] + nums[r] + nums[i]
                if abs(curSum- target) < abs(curMinDiff):
                    curMinDiff = curSum - target
                if curSum < target:
                    l += 1
                else:
                    r -= 1
        return target + curMinDiff
                
            