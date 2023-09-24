class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_needed = dict() # key = complement_needed, val = index
        for i, n in enumerate(nums):
            if n in complement_needed:
                return [i, complement_needed[n]]
            complement_needed[target - n] = i